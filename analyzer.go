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
func analyzeSaveData(jsonData string) (*Result, error) {
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

	var completion int
	result := make(map[string][]*Data, len(ListOrder))

	var heartObtained, silkObtained int
	for _, checkItem := range checkItems {
		evidenceCompleted := checkEvidence(checkItem, serializedList, saveData, questData)
		storyEventCompleted := checkStoryEvent(checkItem, storyEvents)

		status := determineStatus(evidenceCompleted, storyEventCompleted)

		itemData := &Data{
			Name:      checkItem.Scene,
			ResStr:    status,
			Completed: status == "已获得",
		}

		// 根据类型分类
		switch checkItem.Type {
		case 0:
			result[NameHeartList] = append(result[NameHeartList], itemData)
			if status == "已获得" {
				heartObtained++
			}
		case 1:
			result[NameSilkList] = append(result[NameSilkList], itemData)
			if status == "已获得" {
				silkObtained++
			}
		case 3: // 忆境纪念盒
			result[NameBoxList] = append(result[NameBoxList], itemData)
		case 4: // 制造金属
			result[NameMetalList] = append(result[NameMetalList], itemData)
		case 5: // 苔莓
			result[NameMossBerry] = append(result[NameMossBerry], itemData)
		case 6: // 跳蚤
			result[NameFlea] = append(result[NameFlea], itemData)
		}
	}
	completion += heartObtained / 4
	completion += silkObtained / 2

	tools := maps.Clone(tools)
	for _, tool := range playerData.Tools.SavedData {
		if tool.Data.IsUnlocked {
			if !tool.Data.IsHidden {
				result[NameTools] = append(result[NameTools], &Data{
					Name:      tools[tool.Name],
					ResStr:    "已获得",
					Completed: true,
				})
				completion++
			}
			delete(tools, tool.Name)
		}
	}
	for _, tool := range upgradedTools {
		delete(tools, tool)
	}
	if playerData.PermadeathMode == 0 {
		delete(tools, "Shell Satchel")
	} else {
		delete(tools, "Dead Mans Purse")
	}
	var toolsNotObtained []*Data
	for _, name := range tools {
		toolsNotObtained = append(toolsNotObtained, &Data{
			Name:   name,
			ResStr: "未获得",
		})
	}
	result[NameTools] = append(toolsNotObtained, result[NameTools]...)
	slices.SortFunc(result[NameTools], func(a, b *Data) int {
		return cmp.Compare(a.Name, b.Name)
	})

	toolEquips := maps.Clone(toolEquips)
	for _, toolEquip := range playerData.ToolEquips.SavedData {
		if toolEquip.Data.IsUnlocked && toolEquips[toolEquip.Name] != "" {
			result[NameToolEquips] = append(result[NameToolEquips], &Data{
				Name:      toolEquips[toolEquip.Name],
				ResStr:    "已获得",
				Completed: true,
			})
			completion++
		}
	}
	for name := range toolEquips {
		if !slices.ContainsFunc(result[NameToolEquips], func(t *Data) bool { return t.Name == toolEquips[name] }) {
			result[NameToolEquips] = append(result[NameToolEquips], &Data{
				Name:   toolEquips[name],
				ResStr: "未获得",
			})
		}
	}

	result[NameOthers] = append(result[NameOthers], &Data{
		Name:      "织针升级",
		ResStr:    strconv.Itoa(playerData.NailUpgrades) + "/4",
		Completed: playerData.NailUpgrades == 4,
	})
	completion += playerData.NailUpgrades

	result[NameOthers] = append(result[NameOthers], &Data{
		Name:      "工具袋升级",
		ResStr:    strconv.Itoa(playerData.ToolPouchUpgrades) + "/4",
		Completed: playerData.ToolPouchUpgrades == 4,
	})
	completion += playerData.ToolPouchUpgrades

	result[NameOthers] = append(result[NameOthers], &Data{
		Name:      "工具包升级",
		ResStr:    strconv.Itoa(playerData.ToolKitUpgrades) + "/4",
		Completed: playerData.ToolKitUpgrades == 4,
	})
	completion += playerData.ToolKitUpgrades

	result[NameOthers] = append(result[NameOthers], &Data{
		Name:      "丝之心",
		ResStr:    strconv.Itoa(playerData.SilkRegenMax) + "/3",
		Completed: playerData.SilkRegenMax == 3,
	})
	completion += playerData.SilkRegenMax

	if playerData.HasNeedolin {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "织忆弦针",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "织忆弦针",
			ResStr: "未获得",
		})
	}

	if playerData.HasDash {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "疾风步",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "疾风步",
			ResStr: "未获得",
		})
	}

	if playerData.HasWalljump {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "蛛攀术",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "蛛攀术",
			ResStr: "未获得",
		})
	}

	if playerData.HasHarpoonDash {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "飞针冲刺",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "飞针冲刺",
			ResStr: "未获得",
		})
	}

	if playerData.HasSuperJump {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "灵丝升腾",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "灵丝升腾",
			ResStr: "未获得",
		})
	}

	if playerData.HasChargeSlash {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:      "蓄力斩",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameAbilities] = append(result[NameAbilities], &Data{
			Name:   "蓄力斩",
			ResStr: "未获得",
		})
	}

	if playerData.HasBoundCrestUpgrader {
		result[NameOthers] = append(result[NameOthers], &Data{
			Name:      "绑定纹章升级器",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameOthers] = append(result[NameOthers], &Data{
			Name:   "绑定纹章升级器",
			ResStr: "未获得",
		})
	}

	if playerData.HasBoundCrestUpgrader {
		result[NameOthers] = append(result[NameOthers], &Data{
			Name:      "永绽花",
			ResStr:    "已获得",
			Completed: true,
		})
		completion++
	} else {
		result[NameOthers] = append(result[NameOthers], &Data{
			Name:   "永绽花",
			ResStr: "未获得",
		})
	}

	ret := &Result{Completion: completion}
	for _, key := range ListOrder {
		ret.Data = append(ret.Data, &Datas{
			Type:     key,
			DataList: result[key],
		})
	}
	return ret, nil
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
	case "11":
		return saveData.PlayerData.BonetownAspidBerryCollected
	case "12":
		return saveData.PlayerData.MosstownAspidBerryCollected
	case "13":
		return saveData.PlayerData.BonegraveAspidBerryCollected
	case "14":
		return saveData.PlayerData.SavedFleaBoneEast05
	case "15":
		return saveData.PlayerData.SavedFleaDock16
	case "16":
		return saveData.PlayerData.SavedFleaDock03D
	case "17":
		return saveData.PlayerData.SavedFleaBoneEast17B
	case "18":
		return saveData.PlayerData.SavedFleaBoneEast10Church
	case "19":
		return saveData.PlayerData.SavedFleaGreymoor15B
	case "20":
		return saveData.PlayerData.SavedFleaGreymoor06
	case "21":
		return saveData.PlayerData.CaravanLechSaved
	case "22":
		return saveData.PlayerData.SavedFleaShellwood03
	case "23":
		return saveData.PlayerData.SavedFleaBelltown04
	case "24":
		return saveData.PlayerData.SavedFleaBone06
	case "25":
		return saveData.PlayerData.SavedFleaAnt03
	case "26":
		return saveData.PlayerData.SavedFleaDust12
	case "27":
		return saveData.PlayerData.SavedFleaPeak05C
	case "28":
		return saveData.PlayerData.SavedFleaUnder21
	case "29":
		return saveData.PlayerData.SavedFleaUnder23
	case "30":
		return saveData.PlayerData.SavedFleaCoral35
	case "31":
		return saveData.PlayerData.SavedFleaCoral24
	case "32":
		return saveData.PlayerData.SavedFleaCrawl06
	case "33":
		return saveData.PlayerData.SavedFleaSlabCell
	case "34":
		return saveData.PlayerData.SavedFleaSlab06
	case "35":
		return saveData.PlayerData.TamedGiantFlea
	case "36":
		return saveData.PlayerData.MetTroupeHunterWild
	case "37":
		return saveData.PlayerData.SavedFleaShadow10
	case "38":
		return saveData.PlayerData.SavedFleaShadow28
	case "39":
		return saveData.PlayerData.SavedFleaDust09
	case "40":
		return saveData.PlayerData.SavedFleaSong14
	case "41":
		return saveData.PlayerData.SavedFleaSong11
	case "42":
		return saveData.PlayerData.SavedFleaLibrary09
	case "43":
		return saveData.PlayerData.SavedFleaLibrary01
	default:
		panic("未知ID: " + evidenceId)
	}
	return false
}

func checkStoryEvent(checkItem CheckItem, storyEvents []struct {
	EventType int     `json:"EventType"`
	PlayTime  float64 `json:"PlayTime"`
	SceneName string  `json:"SceneName"`
}) bool {
	if checkItem.Type >= 4 || storyEvents == nil {
		return true
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
	if evidenceCompleted {
		if storyEventCompleted {
			return "已获得"
		} else {
			return "疑似BUG"
		}
	}
	return "未获得"
}
