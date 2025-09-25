package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	ColorGreen = "\033[32m"
	ColorRed   = "\033[31m"
	ColorReset = "\033[0m"
)

// getInput 获取用户输入的文件路径
func getInput() string {
	if len(os.Args) != 2 {
		fmt.Println(`请输入存档文件的相对路径 user1.dat 或者完整路径 C:\Users\User\AppData\LocalLow\StudioFOW\Team Cherry\Hollow Knight Silksong\12345678\user1.dat`)
		reader := bufio.NewReader(os.Stdin)
		input, _ := reader.ReadString('\n')
		return strings.TrimSpace(input)
	}
	return os.Args[1]
}

// printItemList 打印物品列表
func printItemList(title string, items []*HiData) (completeCount int) {
	fmt.Println(title)
	for _, item := range items {
		color := ColorRed
		if item.ResStr == "已完成" {
			color = ColorGreen
			completeCount++
		}
		fmt.Printf("%s【%s】%s%s\n", color, item.ResStr, ColorReset, item.Scene)
	}
	fmt.Println("====================")
	return
}

// displayResults 显示分析结果
func displayResults(result *HiResult) {
	printItemList("面具碎片", result.HeartList)
	printItemList("制造金属", result.MetalList)
	printItemList("忆境纪念盒", result.BoxList)
	printItemList("丝轴碎片", result.SilkList)

	fmt.Println("按回车键退出...")
	fmt.Scanln()
}
