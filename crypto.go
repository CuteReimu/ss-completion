package main

import (
	"crypto/aes"
	"encoding/base64"
	"fmt"
	"os"
)

var cSharpFileHeader = []byte{0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0, 0}
var encryptionKey = []byte("UKu52ePUBwetZ9wNX88o54dnfKRu0T1l")

// pkcs7Unpad 移除 PKCS7 填充
func pkcs7Unpad(data []byte, blockSize int) ([]byte, error) {
	if len(data) == 0 || len(data)%blockSize != 0 {
		return nil, fmt.Errorf("invalid padding size")
	}
	padLen := int(data[len(data)-1])
	if padLen == 0 || padLen > blockSize {
		return nil, fmt.Errorf("invalid padding")
	}
	for _, paddingByte := range data[len(data)-padLen:] {
		if int(paddingByte) != padLen {
			return nil, fmt.Errorf("invalid padding")
		}
	}
	return data[:len(data)-padLen], nil
}

// isAlphaNumeric 检查字符是否为字母数字
func isAlphaNumeric(char byte) bool {
	return (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9') || char == '+' || char == '/' || char == '='
}

// decryptFile 解密存档文件
func decryptFile(filename string) (*Result, error) {
	fileContent, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}

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
	encryptedData, err := base64.StdEncoding.DecodeString(string(base64Data))
	if err != nil {
		return nil, err
	}

	// 创建 AES 密码块
	cipher, err := aes.NewCipher(encryptionKey)
	if err != nil {
		return nil, err
	}

	if len(encryptedData)%aes.BlockSize != 0 {
		return nil, fmt.Errorf("encrypted data is not a multiple of block size")
	}

	// 解密数据
	decryptedData := make([]byte, len(encryptedData))
	for blockStart, blockEnd := 0, aes.BlockSize; blockStart < len(encryptedData); blockStart, blockEnd = blockStart+aes.BlockSize, blockEnd+aes.BlockSize {
		cipher.Decrypt(decryptedData[blockStart:blockEnd], encryptedData[blockStart:blockEnd])
	}

	// 移除填充
	unpaddedData, err := pkcs7Unpad(decryptedData, aes.BlockSize)
	if err != nil {
		return nil, err
	}

	return analyzeSaveData(string(unpaddedData))
}
