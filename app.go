package main

import (
	"context"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"

	wailsRuntime "github.com/wailsapp/wails/v2/pkg/runtime"
)

// App struct
type App struct {
	ctx context.Context
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
