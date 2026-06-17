package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"

	"github.com/pkg/errors"
	wailsRuntime "github.com/wailsapp/wails/v2/pkg/runtime"
)

// App struct
type App struct {
	ctx context.Context
	buf []byte
}

// NewApp creates a new App application struct
func NewApp() *App {
	return &App{}
}

// startup is called when the app starts. The context is saved
// so we can call the runtime methods
func (a *App) startup(ctx context.Context) {
	a.ctx = ctx
}

func (a *App) OpenDataFolder() error {
	homeDir, err := os.UserHomeDir()
	if err != nil {
		return err
	}
	homeDir = filepath.Join(homeDir, "AppData/LocalLow/Team Cherry/Hollow Knight Silksong")
	var cmd *exec.Cmd
	switch runtime.GOOS {
	case "windows":
		cmd = exec.Command("explorer", homeDir)
	case "darwin":
		cmd = exec.Command("open", homeDir)
	case "linux":
		cmd = exec.Command("xdg-open", homeDir)
	default:
		return fmt.Errorf("不支持的操作系统: %s", runtime.GOOS)
	}
	return cmd.Start()
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
	if err := os.WriteFile("silksong_user_data.json", buf, 0644); err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	if _, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
		Type:    wailsRuntime.InfoDialog,
		Title:   "提示",
		Message: "已生成silksong_user_data.json",
	}); err != nil {
		wailsRuntime.LogError(a.ctx, err.Error())
	}
}

func (a *App) ModifyScript() {
	_, err := os.Stat("silksong.py")
	if err != nil {
		if !errors.Is(err, os.ErrNotExist) {
			a.errorDialog("导出文件失败")
			return
		}
	} else {
		if v, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
			Type:          wailsRuntime.QuestionDialog,
			Title:         "提示",
			Message:       "检测到silksong.py已存在，是否覆盖？",
			Buttons:       []string{"Yes", "No"},
			DefaultButton: "Yes",
			CancelButton:  "No",
		}); err != nil {
			wailsRuntime.LogError(a.ctx, err.Error())
		} else if v != "Yes" {
			return
		}
	}
	if err := os.WriteFile("silksong.py", starlarkContent, 0644); err != nil {
		a.errorDialog("导出文件失败")
		return
	}
	if _, err := wailsRuntime.MessageDialog(a.ctx, wailsRuntime.MessageDialogOptions{
		Type:    wailsRuntime.ErrorDialog,
		Title:   "提示",
		Message: "已生成silksong.py，请自行编辑即可，编辑后不要忘了保存。",
	}); err != nil {
		wailsRuntime.LogError(a.ctx, err.Error())
	}
}
