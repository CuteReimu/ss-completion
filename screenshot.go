package main

import (
	"encoding/base64"
	"errors"
	"log/slog"

	"golang.design/x/clipboard"
)

var errScreenshotFailed = errors.New("截屏失败")

func (a *App) SaveScreenshot(base64Data string) error {
	if len(base64Data) > 22 && base64Data[:22] == "data:image/png;base64," {
		base64Data = base64Data[22:]
	} else {
		return errScreenshotFailed
	}
	imgData, err := base64.StdEncoding.DecodeString(base64Data)
	if err != nil {
		slog.Error("base64 解码失败", "error", err)
		return errScreenshotFailed
	}
	<-clipboard.Write(clipboard.FmtImage, imgData)
	return nil
}
