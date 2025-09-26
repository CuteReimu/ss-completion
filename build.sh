#!/bin/sh
GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o 丝之歌完成度解析.exe github.com/CuteReimu/ss-completion