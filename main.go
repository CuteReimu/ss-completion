package main

import (
	"fmt"
)

func main() {
	// 获取用户输入
	filename := getInput()

	// 解密存档文件
	result, err := decryptFile(filename)
	if err != nil {
		fmt.Println(err)
		fmt.Println("按回车键退出...")
		fmt.Scanln()
		return
	}

	// 显示分析结果
	displayResults(result)
}
