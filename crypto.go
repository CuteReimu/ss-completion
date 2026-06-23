package main

import (
	"crypto/aes"
	_ "embed"
	"encoding/base64"
	"fmt"
	"log/slog"
	"os"
	"strings"
	"time"

	"github.com/pkg/errors"
	"go.starlark.net/lib/json"
	"go.starlark.net/starlark"
)

var (
	//go:embed silksong.py
	starlarkContentSilksong []byte
	//go:embed hollow.py
	starlarkContentHollow []byte
)
var cSharpFileHeader = []byte{0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0, 0}
var encryptionKey = []byte("UKu52ePUBwetZ9wNX88o54dnfKRu0T1l")

// pkcs7Unpad 移除 PKCS7 填充
func pkcs7Unpad(data []byte, blockSize int) ([]byte, error) {
	if len(data) == 0 || len(data)%blockSize != 0 {
		return nil, errors.New("invalid padding size")
	}
	padLen := int(data[len(data)-1])
	if padLen == 0 || padLen > blockSize {
		return nil, errors.New("invalid padding")
	}
	for _, paddingByte := range data[len(data)-padLen:] {
		if int(paddingByte) != padLen {
			return nil, errors.New("invalid padding")
		}
	}
	return data[:len(data)-padLen], nil
}

// isAlphaNumeric 检查字符是否为字母数字
func isAlphaNumeric(char byte) bool {
	return (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9') || char == '+' || char == '/' || char == '='
}

func (a *App) decryptFile(fileContent string) (*AnalyzeResult, error) {
	buf, err := a.doDecryptFile(fileContent)
	if err != nil {
		slog.Error("doDecryptFile failed", "error", err)
		a.errorDialog(err.Error())
		return nil, err
	}
	a.buf = buf
	result, err := a.analyze(buf)
	if err != nil {
		if !a.isHollow() && err.Error() == `key "Tools" not in dict` {
			a.errorDialog("似乎不是丝之歌的存档")
			return nil, errors.New("似乎不是丝之歌的存档")
		}
		slog.Error("analyze failed", "error", err)
		a.errorDialog(err.Error())
		return nil, err
	}
	return result, nil
}

// doDecryptFile 解密存档文件
func (a *App) doDecryptFile(fileContent string) ([]byte, error) {
	// 查找 Base64 数据的开始和结束位置
	base64Start := len(cSharpFileHeader)
	base64End := len(fileContent) - 1
	for base64Start < base64End && !isAlphaNumeric(fileContent[base64Start]) {
		base64Start++
	}
	for base64End > base64Start && !isAlphaNumeric(fileContent[base64End]) {
		base64End--
	}

	base64Data := fileContent[base64Start : base64End+1]
	encryptedData, err := base64.StdEncoding.DecodeString(base64Data)
	if err != nil {
		return nil, err
	}

	// 创建 AES 密码块
	cipher, err := aes.NewCipher(encryptionKey)
	if err != nil {
		return nil, err
	}

	if len(encryptedData)%aes.BlockSize != 0 {
		return nil, errors.New("encrypted data is not a multiple of block size")
	}

	// 解密数据
	decryptedData := make([]byte, len(encryptedData))
	for blockStart, blockEnd := 0, aes.BlockSize; blockStart < len(encryptedData); blockStart, blockEnd = blockStart+aes.BlockSize, blockEnd+aes.BlockSize {
		cipher.Decrypt(decryptedData[blockStart:blockEnd], encryptedData[blockStart:blockEnd])
	}

	return pkcs7Unpad(decryptedData, aes.BlockSize)
}

type AnalyzeResult struct {
	Completion int
	PlayTime   string
	Categories []*CategoryResult
}

type CategoryResult struct {
	Name  string       `json:"name"`
	Items []ItemResult `json:"items"`
}

type ItemResult struct {
	ShowText   string `json:"show_text"`
	Status     int    `json:"status"` // 0-红色，1-黄色，2-绿色
	StatusText string `json:"status_text"`
	Icon       string `json:"icon"`
	Desc       string `json:"desc"`
	Wiki       string `json:"wiki"`
	Scene      string `json:"scene"`
}

func (a *App) analyzeItems(m map[string][]ItemResult, thread *starlark.Thread, items starlark.Value, starBuf starlark.Value) (int, error) {
	var totalCompletion int
	for item := range starlark.Elements(items.(starlark.Iterable)) {
		var (
			name, category string
			cur, total     = 0, 1
			multiple       = 1
			status         int
			statusText     string
			icon, wiki     string
			desc, scene    string
		)
		d := item.(*starlark.Dict)
		if v, ok, err := d.Get(starlark.String("name")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			name, _ = starlark.AsString(v)
		}
		if v, ok, err := d.Get(starlark.String("category")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			category, _ = starlark.AsString(v)
		}
		if v, ok, err := d.Get(starlark.String("total")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			if err = starlark.AsInt(v, &total); err != nil {
				return 0, errors.WithStack(err)
			}
		}
		if v, ok, err := d.Get(starlark.String("cur")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			result, err := starlark.Call(thread, v.(*starlark.Function), starlark.Tuple{starBuf}, nil)
			if err != nil {
				return 0, errors.WithStack(err)
			}
			if b, ok := result.(starlark.Bool); ok {
				if b {
					cur = total
				}
			} else if err = starlark.AsInt(result, &cur); err != nil {
				return 0, errors.WithStack(err)
			}
		} else {
			return 0, errors.Errorf("%s没有cur函数", name)
		}
		if v, ok, err := d.Get(starlark.String("multiple")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			if err = starlark.AsInt(v, &multiple); err != nil {
				return 0, errors.WithStack(err)
			}
		}
		if v, ok, err := d.Get(starlark.String("icon")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			icon, _ = starlark.AsString(v)
		}
		if v, ok, err := d.Get(starlark.String("desc")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			desc, _ = starlark.AsString(v)
		}
		if v, ok, err := d.Get(starlark.String("scene")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			scene, _ = starlark.AsString(v)
		}
		if v, ok, err := d.Get(starlark.String("wiki")); err != nil {
			return 0, errors.WithStack(err)
		} else if ok {
			wiki, _ = starlark.AsString(v)
		}
		switch {
		case cur >= total:
			status = 2
		case cur > 0:
			status = 1
		}
		switch {
		case total == 1 && cur < total:
			statusText = "未" + getObtainedWord(a.currentGame, category, name)
		case total == 1:
			statusText = "已" + getObtainedWord(a.currentGame, category, name)
		default:
			statusText = fmt.Sprintf("%d/%d", cur, total)
		}
		totalCompletion += cur * multiple
		m[category] = append(m[category], ItemResult{
			ShowText:   name,
			Status:     status,
			StatusText: statusText,
			Icon:       icon,
			Desc:       desc,
			Wiki:       wiki,
			Scene:      scene,
		})
	}
	return totalCompletion, nil
}

func getObtainedWord(gameName, category, name string) string {
	switch category {
	case "跳蚤":
		return "找到"
	case "幼虫":
		return "解救"
	case "Boss", "战士之梦", "守梦者":
		return "击败"
	case "愚人竞技场":
		return "通过"
	case "其它":
		if gameName == "hollow" {
			return "达成"
		}
	}
	if gameName == "hollow" && strings.HasSuffix(name, "万神殿") {
		return "通过"
	}
	return "获得"
}

func (a *App) analyze(buf []byte) (ret *AnalyzeResult, err error) {
	defer func() {
		if r := recover(); r != nil {
			err = errors.Errorf("%s", r)
		}
	}()
	fileName := a.currentGame + ".py"
	starlarkContent, err := os.ReadFile(fileName)
	if err != nil {
		if !errors.Is(err, os.ErrNotExist) {
			return nil, errors.WithStack(err)
		}
		starlarkContent = starlarkContentSilksong
		if a.isHollow() {
			starlarkContent = starlarkContentHollow
		}
	}
	thread := new(starlark.Thread)
	starBuf, err := starlark.Call(thread, json.Module.Members["decode"], starlark.Tuple{starlark.String(buf)}, nil)
	if err != nil {
		return nil, errors.WithStack(err)
	}
	global, err := starlark.ExecFile(thread, fileName, starlarkContent, nil)
	if err != nil {
		return nil, errors.WithStack(err)
	}
	m := make(map[string][]ItemResult)
	totalCompletion, err := a.analyzeItems(m, thread, global["items"], starBuf)
	if err != nil {
		return nil, err
	}
	_, err = a.analyzeItems(m, thread, global["other_items"], starBuf)
	if err != nil {
		return nil, err
	}
	playerData, _, err := starBuf.(*starlark.Dict).Get(starlark.String("playerData"))
	if err != nil {
		return nil, errors.WithStack(err)
	}
	playTimeValue, _, err := playerData.(*starlark.Dict).Get(starlark.String("playTime"))
	if err != nil {
		return nil, errors.WithStack(err)
	}
	playTime := time.Duration(playTimeValue.(starlark.Float)) * time.Second
	ret = &AnalyzeResult{
		Completion: totalCompletion,
		PlayTime:   playTime.String(),
		Categories: make([]*CategoryResult, 0, len(m)),
	}
	for categoryName := range starlark.Elements(global["categories"].(starlark.Iterable)) {
		name, _ := starlark.AsString(categoryName)
		ret.Categories = append(ret.Categories, &CategoryResult{
			Name:  name,
			Items: m[name],
		})
	}
	return ret, nil
}

func init() {
	starlark.Universe["json"] = json.Module
}
