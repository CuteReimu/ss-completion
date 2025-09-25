package main

import (
	"encoding/json"
	"fmt"
	"slices"
)

// analyzeSaveData 分析存档数据并返回结果
func analyzeSaveData(jsonData string) (*HiResult, error) {
	var saveData Data
	if err := json.Unmarshal([]byte(jsonData), &saveData); err != nil {
		return nil, fmt.Errorf("JSON解析错误: %w", err)
	}

	playerData := saveData.PlayerData
	sceneData := saveData.SceneData
	storyEvents := playerData.StoryEvents
	persistentBools := sceneData.PersistentBools
	serializedList := persistentBools.SerializedList
	questCompletion := playerData.QuestCompletionData
	questData := questCompletion.SavedData

	result := &HiResult{}

	for _, checkItem := range checkItems {
		evidenceCompleted := checkEvidence(checkItem, serializedList, saveData, questData)
		storyEventCompleted := checkStoryEvent(checkItem, storyEvents)

		status := determineStatus(evidenceCompleted, storyEventCompleted)

		itemData := &HiData{
			CheckId: checkItem.CheckId,
			Scene:   checkItem.Scene,
			Axis:    checkItem.Axis,
			ResStr:  status,
		}

		// 根据类型分类
		switch checkItem.Type {
		case 0: // 面具碎片
			result.HeartList = append(result.HeartList, itemData)
		case 1: // 丝轴碎片
			result.SilkList = append(result.SilkList, itemData)
		case 3: // 忆境纪念盒
			result.BoxList = append(result.BoxList, itemData)
		case 4: // 制造金属
			result.MetalList = append(result.MetalList, itemData)
		}
	}

	return result, nil
}

// checkEvidence 检查证据是否完成
func checkEvidence(checkItem CheckItem, serializedList []struct {
	ID        string `json:"ID"`
	Mutator   int    `json:"Mutator"`
	SceneName string `json:"SceneName"`
	Value     bool   `json:"Value"`
}, saveData Data, questData []struct {
	Data struct {
		CompletedCount   int  `json:"CompletedCount"`
		HasBeenSeen      bool `json:"HasBeenSeen"`
		IsAccepted       bool `json:"IsAccepted"`
		IsCompleted      bool `json:"IsCompleted"`
		WasEverCompleted bool `json:"WasEverCompleted"`
	} `json:"Data"`
	Name string `json:"Name"`
}) bool {
	switch checkItem.Evi {
	case 0: // 场景物品
		itemIndex := slices.IndexFunc(serializedList, func(persistentItem struct {
			ID        string `json:"ID"`
			Mutator   int    `json:"Mutator"`
			SceneName string `json:"SceneName"`
			Value     bool   `json:"Value"`
		}) bool {
			return persistentItem.SceneName == checkItem.Evidence1 && persistentItem.ID == checkItem.Evidence2
		})
		return itemIndex >= 0 && serializedList[itemIndex].Value

	case 1: // 商店购买
		return checkShopPurchase(checkItem.Evidence2, saveData)

	case 2: // 任务完成
		questIndex := slices.IndexFunc(questData, func(questItem struct {
			Data struct {
				CompletedCount   int  `json:"CompletedCount"`
				HasBeenSeen      bool `json:"HasBeenSeen"`
				IsAccepted       bool `json:"IsAccepted"`
				IsCompleted      bool `json:"IsCompleted"`
				WasEverCompleted bool `json:"WasEverCompleted"`
			} `json:"Data"`
			Name string `json:"Name"`
		}) bool {
			return questItem.Name == checkItem.Evidence2
		})
		return questIndex >= 0 && questData[questIndex].Data.IsCompleted && questData[questIndex].Data.WasEverCompleted
	}

	return false
}

// checkShopPurchase 检查商店购买状态
func checkShopPurchase(evidenceId string, saveData Data) bool {
	switch evidenceId {
	case "1":
		return saveData.PlayerData.PurchasedBonebottomHeartPiece
	case "2":
		return saveData.PlayerData.PurchasedBonebottomToolMetal
	case "3":
		return saveData.PlayerData.PurchasedPilgrimsRestMemoryLocket
	case "4":
		return saveData.PlayerData.PurchasedBelltownMemoryLocket
	case "5":
		return saveData.PlayerData.PurchasedBelltownSpoolSegment
	case "6":
		return saveData.PlayerData.MerchantEnclaveShellFragment
	case "7":
		return saveData.PlayerData.PurchasedGrindleSpoolPiece
	case "8":
		return saveData.PlayerData.MetCaravanTroupeLeaderJudge
	case "9":
		return saveData.PlayerData.MerchantEnclaveToolMetal
	case "10":
		return saveData.PlayerData.MerchantEnclaveSpoolPiece
	}
	return false
}

// checkStoryEvent 检查故事事件
func checkStoryEvent(checkItem CheckItem, storyEvents []struct {
	EventType int     `json:"EventType"`
	PlayTime  float64 `json:"PlayTime"`
	SceneName string  `json:"SceneName"`
}) bool {
	if checkItem.Type == 4 || storyEvents == nil {
		return true // 制造金属不需要故事事件检查
	}

	return slices.ContainsFunc(storyEvents, func(storyEvent struct {
		EventType int     `json:"EventType"`
		PlayTime  float64 `json:"PlayTime"`
		SceneName string  `json:"SceneName"`
	}) bool {
		return storyEvent.EventType == checkItem.Type && storyEvent.SceneName == checkItem.Evidence1
	})
}

// determineStatus 确定完成状态
func determineStatus(evidenceCompleted, storyEventCompleted bool) string {
	if evidenceCompleted && storyEventCompleted {
		return "已完成"
	} else if evidenceCompleted && !storyEventCompleted {
		return "疑似BUG"
	}
	return "未完成"
}
