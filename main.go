package main

import (
	"embed"
	"fmt"
	"log"
	"log/slog"
	"os"
	"runtime"

	"github.com/wailsapp/wails/v2"
	"github.com/wailsapp/wails/v2/pkg/options"
	"github.com/wailsapp/wails/v2/pkg/options/assetserver"
)

//go:embed all:frontend/dist
var assets embed.FS

func main() {
	// Create an instance of the app structure
	app := NewApp()

	if runtime.GOOS == "windows" && len(os.Args) > 1 {
		app.initialFile = os.Args[1]
	}

	// Create application with options
	err := wails.Run(&options.App{
		Title:  "空洞骑士丝之歌存档分析器",
		Width:  1400,
		Height: 900,
		AssetServer: &assetserver.Options{
			Assets: assets,
		},
		DragAndDrop: &options.DragAndDrop{
			EnableFileDrop:     true,
			DisableWebViewDrop: true,
		},
		OnStartup: app.startup,
		Bind:      []any{app},
	})

	if err != nil {
		println("Error:", err.Error())
	}
}

func init() {
	log.SetFlags(log.Flags() | log.Lshortfile)
	jsonHandler := slog.NewJSONHandler(os.Stderr, &slog.HandlerOptions{
		AddSource: true,
		ReplaceAttr: func(groups []string, attr slog.Attr) slog.Attr {
			if attr.Key == "error" {
				if err, ok := attr.Value.Any().(error); ok {
					return slog.Attr{
						Key:   "error",
						Value: slog.StringValue(fmt.Sprintf("%+v", err)),
					}
				}
			}
			return attr
		},
	})
	slog.SetDefault(slog.New(jsonHandler))
}
