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
		fmt.Printf("解密失败: %v\n", err)
		return
	}

	// 显示分析结果
	displayResults(result)
}
