package main

import (
	"bufio"
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"strings"
	"text/template"
	"time"
)

var (
	//go:embed static
	htmlFiles embed.FS
	//go:embed result.html
	resultTemplateFile string
)

func initWebUI(htmlResult string) {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/html; charset=utf-8")
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(htmlResult))
	})
	mux.Handle("/x/", http.StripPrefix("/x/", http.FileServer(http.FS(htmlFiles))))

	go func() {
		if err := http.ListenAndServe("127.0.0.1:12332", mux); err != nil {
			panic(err)
		}
	}()
}

// getInput 获取用户输入的文件路径
func getInput() string {
	if len(os.Args) != 2 {
		fmt.Println(`请输入存档文件的相对路径 user1.dat 或者完整路径 C:\Users\User\AppData\LocalLow\Team Cherry\Hollow Knight Silksong\12345678\user1.dat，回车键确认`)
		fmt.Println("小技巧：可以直接将文件拖拽到此窗口，会直接填入路径")
		reader := bufio.NewReader(os.Stdin)
		input, _ := reader.ReadString('\n')
		return strings.Trim(strings.TrimSpace(input), "\"")
	}
	return os.Args[1]
}

// displayResults 显示分析结果
func displayResults(result *HiResult) {
	buf, _ := json.MarshalIndent(result, "", "  ")
	var b bytes.Buffer
	err := htmlTemplate.Execute(&b, map[string]any{"Data": string(buf)})
	if err != nil {
		fmt.Println(err)
		fmt.Println("按回车键退出...")
		fmt.Scanln()
		return
	}
	htmlResult := b.String()
	initWebUI(htmlResult)
	switch strings.ToLower(runtime.GOOS) {
	case "windows":
		_ = exec.Command("rundll32", "url.dll,FileProtocolHandler", "http://127.0.0.1:12332/").Start()
	case "linux":
		_ = exec.Command("xdg-open", "http://127.0.0.1:12332/").Start()
	case "darwin":
		_ = exec.Command("open", "http://127.0.0.1:12332/").Start()
	default:
		fmt.Println("不支持自动打开浏览器的操作系统：", runtime.GOOS)
		fmt.Println("请手动打开浏览器并访问: http://127.0.0.1:12332/")
	}
	time.AfterFunc(3*time.Second, func() {
		fmt.Println("按回车键退出...")
	})
	fmt.Scanln()
}

var (
	htmlTemplate *template.Template
)

func init() {
	t, err := template.New("result").Parse(resultTemplateFile)
	if err != nil {
		panic(t)
	}
	htmlTemplate = t
}
