# 空洞骑士：丝之歌存档完成度分析工具

本仓库实际上是把 https://github.com/nov1ce-lee/hollowKnightSaveParser 打包成桌面版。

## 克隆仓库

```bash
# 注意要加 --recursive 参数
git clone --recursive https://github.com/CuteReimu/ss-completion.git
```

## 编译说明

首先需要 Go 和 Nodejs，然后安装 wails：

```bash
go install github.com/wailsapp/wails/v2/cmd/wails@latest
```

然后使用以下命令就可以调试或打包了：

```bash
# 本地调试
wails dev

# 打包
wails build -platform=windows/amd64 -webview2 embed
```
