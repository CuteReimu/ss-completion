# 空洞骑士：丝之歌存档完成度分析工具

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

## 如何贡献

- 打开存档分析器，点击修改脚本按钮，然后会生成一个`silksong.py`/`hollow.py`文件，自行修改即可。注释很清晰，一眼就能看懂。
   - `silksong.py`/`hollow.py`实际上是 [Starlark](https://github.com/bazelbuild/starlark) 脚本，语法和Python基本相同。
- 考虑到你们可能不知道存档的数据结构是什么样的，可以把自己存档导入后，点击导出解析后的存档，就会导出一个json文件，就知道是什么数据结构了。有了这个就可以更方便的自定义脚本了。
- 修改好之后自己就能进行测试，无需重启本工具。测试无误后即可使用PR的方式提交到本仓库。
