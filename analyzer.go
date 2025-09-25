package main

import (
	"cmp"
	"encoding/json"
	"fmt"
	"maps"
	"slices"
	"strconv"
)

// analyzeSaveData 分析存档数据并返回结果
func analyzeSaveData(jsonData string) (*HiResult, error) {
	var saveData SaveData
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

	var heartObtained, silkObtained int
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
		case 0:
			result.HeartList = append(result.HeartList, itemData)
			if status == "已获得" {
				heartObtained++
			}
		case 1:
			result.SilkList = append(result.SilkList, itemData)
			if status == "已获得" {
				silkObtained++
			}
		case 3: // 忆境纪念盒
			result.BoxList = append(result.BoxList, itemData)
		case 4: // 制造金属
			result.MetalList = append(result.MetalList, itemData)
		}
	}
	result.Completion += heartObtained / 4
	result.Completion += silkObtained / 2

	tools := maps.Clone(tools)
	for _, tool := range playerData.Tools.SavedData {
		if tool.Data.IsUnlocked {
			if !tool.Data.IsHidden {
				result.Tools = append(result.Tools, &ToolData{
					Name:   tools[tool.Name],
					ResStr: "已获得",
				})
				result.Completion++
			}
			delete(tools, tool.Name)
		}
	}
	for _, tool := range upgradedTools {
		delete(tools, tool)
	}
	var toolsNotObtained []*ToolData
	for _, name := range tools {
		toolsNotObtained = append(toolsNotObtained, &ToolData{
			Name:   name,
			ResStr: "未获得",
		})
	}
	result.Tools = append(toolsNotObtained, result.Tools...)
	slices.SortFunc(result.Tools, func(a, b *ToolData) int {
		return cmp.Compare(a.Name, b.Name)
	})

	toolEquips := maps.Clone(toolEquips)
	for _, toolEquip := range playerData.ToolEquips.SavedData {
		if toolEquip.Data.IsUnlocked && toolEquips[toolEquip.Name] != "" {
			result.ToolEquips = append(result.ToolEquips, &ToolData{
				Name:   toolEquips[toolEquip.Name],
				ResStr: "已获得",
			})
			result.Completion++
		}
	}
	for name := range toolEquips {
		if !slices.ContainsFunc(result.ToolEquips, func(t *ToolData) bool { return t.Name == toolEquips[name] }) {
			result.ToolEquips = append(result.ToolEquips, &ToolData{
				Name:   toolEquips[name],
				ResStr: "未获得",
			})
		}
	}

	result.Others = append(result.Others, &OtherData{
		Name:      "织针升级",
		ResStr:    strconv.Itoa(playerData.NailUpgrades) + "/4",
		Completed: playerData.NailUpgrades == 4,
	})
	result.Completion += playerData.NailUpgrades

	result.Others = append(result.Others, &OtherData{
		Name:      "工具袋升级",
		ResStr:    strconv.Itoa(playerData.ToolPouchUpgrades) + "/4",
		Completed: playerData.ToolPouchUpgrades == 4,
	})
	result.Completion += playerData.ToolPouchUpgrades

	result.Others = append(result.Others, &OtherData{
		Name:      "工具包升级",
		ResStr:    strconv.Itoa(playerData.ToolKitUpgrades) + "/4",
		Completed: playerData.ToolKitUpgrades == 4,
	})
	result.Completion += playerData.ToolKitUpgrades

	result.Others = append(result.Others, &OtherData{
		Name:      "丝之心",
		ResStr:    strconv.Itoa(playerData.SilkRegenMax) + "/3",
		Completed: playerData.SilkRegenMax == 3,
	})
	result.Completion += playerData.SilkRegenMax

	if playerData.HasNeedolin {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "织忆弦针",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "织忆弦针",
			ResStr: "未获得",
		})
	}

	if playerData.HasDash {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "疾风步",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "疾风步",
			ResStr: "未获得",
		})
	}

	if playerData.HasWalljump {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "蛛攀术",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "蛛攀术",
			ResStr: "未获得",
		})
	}

	if playerData.HasHarpoonDash {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "飞针冲刺",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "飞针冲刺",
			ResStr: "未获得",
		})
	}

	if playerData.HasSuperJump {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "灵丝升腾",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "灵丝升腾",
			ResStr: "未获得",
		})
	}

	if playerData.HasChargeSlash {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "蓄力斩",
			ResStr: "已获得",
		})
		result.Completion++
	} else {
		result.Abilities = append(result.Abilities, &ToolData{
			Name:   "蓄力斩",
			ResStr: "未获得",
		})
	}

	if playerData.HasBoundCrestUpgrader {
		result.Others = append(result.Others, &OtherData{
			Name:      "绑定纹章升级器",
			ResStr:    "已获得",
			Completed: true,
		})
		result.Completion++
	} else {
		result.Others = append(result.Others, &OtherData{
			Name:   "绑定纹章升级器",
			ResStr: "未获得",
		})
	}

	if playerData.HasBoundCrestUpgrader {
		result.Others = append(result.Others, &OtherData{
			Name:      "永绽花",
			ResStr:    "已获得",
			Completed: true,
		})
		result.Completion++
	} else {
		result.Others = append(result.Others, &OtherData{
			Name:   "永绽花",
			ResStr: "未获得",
		})
	}

	return result, nil
}

func checkEvidence(checkItem CheckItem, serializedList []struct {
	ID        string `json:"ID"`
	Mutator   int    `json:"Mutator"`
	SceneName string `json:"SceneName"`
	Value     bool   `json:"Value"`
}, saveData SaveData, questData []struct {
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

	case 1:
		return checkShopPurchase(checkItem.Evidence2, saveData)

	case 2:
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

func checkShopPurchase(evidenceId string, saveData SaveData) bool {
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

func determineStatus(evidenceCompleted, storyEventCompleted bool) string {
	if evidenceCompleted && storyEventCompleted {
		return "已获得"
	} else if evidenceCompleted && !storyEventCompleted {
		return "疑似BUG"
	}
	return "未获得"
}
