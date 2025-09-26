# 空洞骑士：丝之歌存档完成度分析工具

这是一个用于分析《空洞骑士：丝之歌》存档文件的**完成度**的 Go 程序。

## 项目结构

- `main.go` - 程序入口，简洁明了
- `crypto.go` - 加密解密相关功能
- `models.go` - 数据模型定义
- `analyzer.go` - 存档分析逻辑
- `ui.go` - 用户界面和输出
- `user_data.go` - 用户数据结构定义

## 使用方法

```bash
# 考虑到cdn访问较慢，不如直接下载打包进去
./download_cdn.sh

# 编译程序
go build -o ss-completion .

# 运行程序
./ss-completion [存档文件路径]

# 如果不提供参数，程序会提示输入文件路径
./ss-completion

# 启动后访问 http://127.0.0.1:12332/ 即可
```
