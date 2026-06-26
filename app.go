package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io/fs"
	"log/slog"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"slices"

	"github.com/pkg/errors"
	wailsRuntime "github.com/wailsapp/wails/v2/pkg/runtime"
)

// App struct
type App struct {
	ctx context.Context
	buf []byte

	selectedFile string
	currentGame  string
	initialFile  string
}

// NewApp creates a new App application struct
func NewApp() *App {
	return &App{currentGame: "silksong"}
}

// startup is called when the app starts. The context is saved
// so we can call the runtime methods
func (a *App) startup(ctx context.Context) {
	a.ctx = ctx
	a.setWindowSize()
}

func (a *App) setWindowSize() {
	// 1. 获取所有屏幕的信息
	screens, _ := wailsRuntime.ScreenGetAll(a.ctx)
	if len(screens) == 0 {
		return // 获取失败，使用默认配置
	}

	// 2. 找到主屏幕 (IsPrimary) 或当前屏幕 (IsCurrent)
	var targetScreen *wailsRuntime.Screen
	for _, screen := range screens {
		if screen.IsPrimary || screen.IsCurrent {
			targetScreen = &screen
			if screen.IsCurrent {
				break
			}
		}
	}
	// 如果没找到主屏幕，就回退使用第一个屏幕
	if targetScreen == nil && len(screens) > 0 {
		targetScreen = &screens[0]
	}
	if targetScreen == nil {
		return
	}

	// 3. 计算高度：屏幕总高度减去 100 像素
	newHeight := targetScreen.Size.Height - 100

	// 防止负高度（比如屏幕高度本身就小于 100，虽然很少见）
	if newHeight < 200 {
		newHeight = targetScreen.Size.Height
	}

	wailsRuntime.WindowSetSize(a.ctx, min(1400, targetScreen.Size.Width), newHeight)
	wailsRuntime.WindowCenter(a.ctx)
}

func (a *App) GetInitialFile() string {
	f := a.initialFile
	a.initialFile = ""
	return f
}

func (a *App) ChangeGame(gameName string) {
	a.currentGame = gameName
}

func (a *App) isHollow() bool {
	return a.currentGame == "hollow"
}

func (a *App) OpenDataFolder() {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		a.errorDialog(err.Error())
		return
	}
	if a.isHollow() {
		homeDir = filepath.Join(homeDir, "AppData/LocalLow/Team Cherry/Hollow Knight")
	} else {
		homeDir = filepath.Join(homeDir, "AppData/LocalLow/Team Cherry/Hollow Knight Silksong")
	}
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "windows":
		cmd = exec.Command("explorer", homeDir)
	case "darwin":
		cmd = exec.Command("open", homeDir)
	case "linux":
		cmd = exec.Command("xdg-open", homeDir)
	default:
		a.errorDialog(fmt.Sprintf("不支持的操作系统: %s", runtime.GOOS))
		return
	}
	go func() {
		_ = cmd.Run()
	}()
}

type Option struct {
	Label string `json:"label"`
	Value string `json:"value"`
}

var userDataFileName = []string{"user1.dat", "user2.dat", "user3.dat", "user4.dat"}

func (a *App) ShowDataFolder() []Option {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		return nil
	}
	if a.isHollow() {
		homeDir = filepath.Join(homeDir, "AppData/LocalLow/Team Cherry/Hollow Knight")
	} else {
		homeDir = filepath.Join(homeDir, "AppData/LocalLow/Team Cherry/Hollow Knight Silksong")
	}
	var ret []Option
	_ = filepath.WalkDir(homeDir, func(path string, info fs.DirEntry, err error) error {
		if err != nil {
			slog.Error("walk dir error", "error", err)
			return nil
		}
		if !info.IsDir() && slices.Contains(userDataFileName, info.Name()) {
			dir, err := filepath.Rel(homeDir, path)
			if err == nil {
				ret = append(ret, Option{Label: dir, Value: path})
			}
		}
		return nil
	})
	return ret
}

func (a *App) RefreshUserData() (*AnalyzeResult, error) {
	buf, err := os.ReadFile(a.selectedFile)
	if err != nil {
		a.errorDialog(err.Error())
		return nil, err
	}
	return a.decryptFile(string(buf))
}

func (a *App) SelectUserData(filePath string) (*AnalyzeResult, error) {
	a.selectedFile = filePath
	buf, err := os.ReadFile(filePath)
	if err != nil {
		a.errorDialog(err.Error())
		return nil, err
	}
	return a.decryptFile(string(buf))
}

func (a *App) ChooseDataFile() (*AnalyzeResult, error) {
	filePath, err := wailsRuntime.OpenFileDialog(a.ctx, wailsRuntime.OpenDialogOptions{
		Filters: []wailsRuntime.FileFilter{{
			DisplayName: "存档文件",
			Pattern:     "*.dat",
		}},
	})
	if err != nil {
		a.errorDialog(err.Error())
		return nil, err
	}
	if filePath == "" {
		return nil, nil
	}
	a.selectedFile = filePath
	buf, err := os.ReadFile(filePath)
	if err != nil {
		a.errorDialog(err.Error())
		return nil, err
	}
	return a.decryptFile(string(buf))
}

func (a *App) errorDialog(s string) {
	if _, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
		Type:    wailsRuntime.ErrorDialog,
		Title:   "错误",
		Message: s,
	}); err != nil {
		wailsRuntime.LogError(a.ctx, s)
	}
}

func (a *App) SaveBuf() {
	if len(a.buf) == 0 {
		a.errorDialog("还未加载user.dat")
		return
	}
	var m any
	err := json.Unmarshal(a.buf, &m)
	if err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	buf, err := json.MarshalIndent(m, "", "\t")
	if err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	fileName := "silksong_user_data.json"
	if a.isHollow() {
		fileName = "hollow_knight_user_data.json"
	}
	if err := os.WriteFile(fileName, buf, 0644); err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	if _, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
		Type:    wailsRuntime.InfoDialog,
		Title:   "提示",
		Message: "已生成" + fileName,
	}); err != nil {
		wailsRuntime.LogError(a.ctx, err.Error())
	}
}

func (a *App) ModifyScript() {
	fileName := a.currentGame + ".py"
	_, err := os.Stat(fileName)
	if err != nil {
		if !errors.Is(err, os.ErrNotExist) {
			a.errorDialog("导出文件失败")
			return
		}
	} else {
		if v, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
			Type:          wailsRuntime.QuestionDialog,
			Title:         "提示",
			Message:       fmt.Sprintf("检测到%s已存在，是否覆盖？", fileName),
			Buttons:       []string{"Yes", "No"},
			DefaultButton: "Yes",
			CancelButton:  "No",
		}); err != nil {
			wailsRuntime.LogError(a.ctx, err.Error())
		} else if v != "Yes" {
			return
		}
	}
	starlarkContent := starlarkContentSilksong
	if a.isHollow() {
		starlarkContent = starlarkContentHollow
	}
	if err := os.WriteFile(fileName, starlarkContent, 0644); err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	if _, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
		Type:    wailsRuntime.InfoDialog,
		Title:   "提示",
		Message: fmt.Sprintf("已生成%s，请自行编辑即可，编辑后不要忘了保存。", fileName),
	}); err != nil {
		wailsRuntime.LogError(a.ctx, err.Error())
	}
}
