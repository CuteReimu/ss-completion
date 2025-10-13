package main

import (
	"encoding/json"
	"fmt"
	"strings"
)

// CheckItem 检查项结构
type CheckItem struct {
	Type      int    `json:"type"`
	Scene     string `json:"scene"`
	Evi       int    `json:"ev"`
	Evidence1 string `json:"ev1"`
	Evidence2 string `json:"ev2"`
}

type Data struct {
	Name      string `json:"name"`
	ResStr    string `json:"resStr"`
	Completed bool   `json:"completed"`
}

type Datas struct {
	Type     string  `json:"type"`
	DataList []*Data `json:"dataList"`
}

const (
	NameHeartList  = "面具碎片"
	NameSilkList   = "灵丝轴碎片"
	NameToolEquips = "纹章（除猎手外）"
	NameTools      = "法术和工具"
	NameAbilities  = "能力"
	NameOthers     = "其它"
	NameMetalList  = "制造金属（不占完成度，但工具必须）"
	NameBoxList    = "忆境纪念盒（不占完成度）"
	NameMossBerry  = "苔莓（不占完成度）"
	NameFlea       = "跳蚤（不占完成度）"
)

var ListOrder = []string{NameHeartList, NameSilkList, NameToolEquips, NameTools, NameAbilities, NameOthers, NameMetalList, NameBoxList, NameMossBerry, NameFlea}

// Result 分析结果
type Result struct {
	Completion int      `json:"completion"`
	Data       []*Datas `json:"data"`
}

// 检查项数据
var checkItems = []CheckItem{
	{Type: 4, Scene: "骸骨洞窟", Evi: 0, Evidence1: "Bone_07", Evidence2: "Collectable Item Pickup - Tool Metal"},
	{Type: 4, Scene: "深坞右侧宝箱", Evi: 0, Evidence1: "Dock_03", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "猎人小径野兽教堂旁", Evi: 0, Evidence1: "Ant_20", Evidence2: "Collectable Item Pickup"},
	{Type: 0, Scene: "远野炸地板", Evi: 0, Evidence1: "Bone_East_20", Evidence2: "Heart Piece"},
	{Type: 0, Scene: "骸底买面具", Evi: 1, Evidence1: "Bonetown", Evidence2: "1"},
	{Type: 4, Scene: "骸底买金属", Evi: 1, Evidence1: "Bonetown", Evidence2: "2"},
	{Type: 0, Scene: "沙虫道_简易钥匙门前（底部隐藏墙）", Evi: 0, Evidence1: "Crawl_02", Evidence2: "Heart Piece"},
	{Type: 3, Scene: "朝圣者憩所购买", Evi: 1, Evidence1: "Bone_East_10_Room", Evidence2: "3"},
	{Type: 0, Scene: "甲木林（下劈花朵连跳）", Evi: 0, Evidence1: "Shellwood_14", Evidence2: "Heart Piece"},
	{Type: 3, Scene: "骸骨洞窟(需螳螂爪)", Evi: 0, Evidence1: "Bone_18", Evidence2: "Collectable Item Pickup"},
	{Type: 0, Scene: "洞窟与深坞之间", Evi: 0, Evidence1: "Dock_08", Evidence2: "Heart Piece"},
	{Type: 3, Scene: "骸底提交暴烈燧甲虫任务", Evi: 2, Evidence1: "Bonetown", Evidence2: "Rock Rollers"},
	{Type: 1, Scene: "出生点织巢", Evi: 0, Evidence1: "Weave_11", Evidence2: "Silk Spool"},
	{Type: 3, Scene: "钟心镇购买盒子", Evi: 1, Evidence1: "Belltown", Evidence2: "4"},
	{Type: 3, Scene: "工厂忏悔机旁光源（打完白愈厅boss向下）", Evi: 0, Evidence1: "Under_08", Evidence2: "Collectable Item Pickup"},
	{Type: 1, Scene: "圣煲工厂", Evi: 0, Evidence1: "Under_10", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "圣扉巨门顶部", Evi: 0, Evidence1: "Song_19_entrance", Evidence2: "Silk Spool"},
	{Type: 3, Scene: "圣煲钟道顶部", Evi: 0, Evidence1: "Bellway_City", Evidence2: "Collectable Item Pickup"},
	{Type: 1, Scene: "圣煲工厂底部", Evi: 0, Evidence1: "Library_11b", Evidence2: "Silk Spool"},
	{Type: 4, Scene: "圣煲工厂", Evi: 0, Evidence1: "Under_19b", Evidence2: "Collectable Item Pickup - Tool Metal"},
	{Type: 1, Scene: "灰沼顶部", Evi: 0, Evidence1: "Greymoor_02", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "白愈厅救谢尔玛", Evi: 2, Evidence1: "Ward_09", Evidence2: "Save Sherma"},
	{Type: 1, Scene: "白愈厅电梯下方", Evi: 0, Evidence1: "Ward_01", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "钟心镇买丝轴", Evi: 1, Evidence1: "Belltown", Evidence2: "5"},
	{Type: 0, Scene: "圣歌盟地买面具", Evi: 1, Evidence1: "Song_Enclave", Evidence2: "6"},
	{Type: 0, Scene: "火灵竹林_最右侧", Evi: 0, Evidence1: "Wisp_07", Evidence2: "Heart Piece"},
	{Type: 4, Scene: "火灵竹林_上方小道旁", Evi: 0, Evidence1: "Wisp_05", Evidence2: "Collectable Item Pickup - Tool Metal"},
	{Type: 1, Scene: "忆廊_左侧翠庭生态区", Evi: 0, Evidence1: "Arborium_09", Evidence2: "Silk Spool"},
	{Type: 3, Scene: "忆廊_中部甲木林生态区", Evi: 0, Evidence1: "Arborium_05", Evidence2: "Collectable Item Pickup"},
	{Type: 4, Scene: "腐殖渠", Evi: 0, Evidence1: "Aqueduct_05", Evidence2: "Collectable Item Pickup - Tool Metal"},
	{Type: 0, Scene: "远野岩浆挑战", Evi: 0, Evidence1: "Bone_East_LavaChallenge", Evidence2: "Heart Piece (1)"},
	{Type: 3, Scene: "腐汁泽左上角", Evi: 0, Evidence1: "Shadow_20", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "腐汁泽打沙包", Evi: 0, Evidence1: "Shadow_27", Evidence2: "Sack Corpse Pickup"},
	{Type: 0, Scene: "腐汁泽（粪海狂蛆跑酷）", Evi: 0, Evidence1: "Shadow_13", Evidence2: "Heart Piece"},
	{Type: 3, Scene: "中途酒馆", Evi: 0, Evidence1: "Halfway_01", Evidence2: "Collectable Item Pickup"},
	{Type: 1, Scene: "蚀阶小偷购买", Evi: 1, Evidence1: "Coral_42", Evidence2: "7"},
	{Type: 3, Scene: "卡拉卡沙川", Evi: 0, Evidence1: "Coral_23", Evidence2: "Collectable Item Pickup"},
	{Type: 4, Scene: "蚀阶（boss门前两铃铛下去）", Evi: 0, Evidence1: "Coral_32", Evidence2: "Collectable Item Pickup - Tool Metal"},
	{Type: 1, Scene: "跳蚤旅团搬到蚀阶", Evi: 1, Evidence1: "Coral_Judge_Arena", Evidence2: "8"},
	{Type: 3, Scene: "灰沼车站左侧", Evi: 0, Evidence1: "Greymoor_16", Evidence2: "Collectable Item Pickup"},
	{Type: 0, Scene: "机枢核心左边", Evi: 0, Evidence1: "Song_09", Evidence2: "Heart Piece"},
	{Type: 0, Scene: "出生点织巢", Evi: 0, Evidence1: "Weave_05b", Evidence2: "Heart Piece"},
	{Type: 0, Scene: "钟心镇猎杀兽蝇任务", Evi: 2, Evidence1: "Belltown", Evidence2: "Beastfly Hunt"},
	{Type: 0, Scene: "图书馆玻璃罐", Evi: 0, Evidence1: "Library_05", Evidence2: "library_glass_heart_piece"},
	{Type: 1, Scene: "高庭顶部", Evi: 0, Evidence1: "Hang_03_top", Evidence2: "Silk Spool"},
	{Type: 4, Scene: "圣歌盟地买金属（需再寻商贾）", Evi: 1, Evidence1: "Song_Enclave", Evidence2: "9"},
	{Type: 1, Scene: "圣歌盟地买丝轴（需再寻商贾）", Evi: 1, Evidence1: "Song_Enclave", Evidence2: "10"},
	{Type: 0, Scene: "罪石监狱上右", Evi: 0, Evidence1: "Slab_17", Evidence2: "Heart Piece"},
	{Type: 1, Scene: "罪石监狱左侧", Evi: 0, Evidence1: "Peak_01", Evidence2: "Silk Spool"},
	{Type: 0, Scene: "雪山柱子内", Evi: 0, Evidence1: "Peak_04c", Evidence2: "Heart Piece"},
	{Type: 0, Scene: "蚀阶（冲刺跳+飞针+二段跳）", Evi: 0, Evidence1: "Coral_19b", Evidence2: "Heart Piece"},
	{Type: 1, Scene: "深坞（熔岩地板房）", Evi: 0, Evidence1: "Bone_East_13", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "德鲁伊下方", Evi: 0, Evidence1: "Bone_11b", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "深坞右侧", Evi: 0, Evidence1: "Dock_03c", Evidence2: "Silk Spool"},
	{Type: 1, Scene: "机枢核心右下", Evi: 0, Evidence1: "Cog_07", Evidence2: "Silk Spool"},
	{Type: 3, Scene: "沙虫道左下", Evi: 0, Evidence1: "Crawl_09", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "蚀阶（下层椅子跳跳乐）", Evi: 0, Evidence1: "Coral_02", Evidence2: "Collectable Item Pickup (1)"},
	{Type: 3, Scene: "图书馆右上", Evi: 0, Evidence1: "Library_08", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "深坞温泉房下方", Evi: 0, Evidence1: "Dock_13", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "罪石监狱", Evi: 0, Evidence1: "Slab_Cell_Quiet", Evidence2: "Collectable Item Pickup"},
	{Type: 3, Scene: "第三幕远野右上方_女王门口右侧", Evi: 0, Evidence1: "Bone_East_25", Evidence2: "Collectable Item Pickup"},
	{Type: 0, Scene: "第三幕飞毛腿赛跑", Evi: 2, Evidence1: "Sprintmaster_Cave", Evidence2: "Sprintmaster Race"},
	{Type: 3, Scene: "第三幕钟心镇上冲", Evi: 0, Evidence1: "Belltown", Evidence2: "Collectable Item Pickup"},
	{Type: 0, Scene: "第三幕雪山洞窟", Evi: 0, Evidence1: "Peak_06", Evidence2: "Heart Piece"},
	{Type: 0, Scene: "第三幕暗蚀之心任务", Evi: 2, Evidence1: "Belltown", Evidence2: "Destroy Thread Cores"},
	{Type: 0, Scene: "第三幕隐秘猎手任务", Evi: 2, Evidence1: "Belltown", Evidence2: "Ant Trapper"},
	{Type: 5, Scene: "忆廊_椅子旁", Evi: 0, Evidence1: "Arborium_04", Evidence2: "moss_berry_fruit"},
	{Type: 5, Scene: "苔穴出生点左上", Evi: 0, Evidence1: "Tut_02", Evidence2: "moss_berry_fruit"},
	{Type: 5, Scene: "出生点织巢左侧", Evi: 0, Evidence1: "Weave_03", Evidence2: "moss_berry_fruit"},
	{Type: 5, Scene: "苔穴出生点右上", Evi: 0, Evidence1: "Tut_01b", Evidence2: "moss_berry_fruit"},
	{Type: 5, Scene: "骸底镇上空_蚊子", Evi: 1, Evidence1: "Bonetown", Evidence2: "11"},
	{Type: 5, Scene: "德鲁伊下方_蚊子", Evi: 1, Evidence1: "Bone_05b", Evidence2: "12"},
	{Type: 5, Scene: "漫游者教堂上空_蚊子", Evi: 1, Evidence1: "Bonegrave", Evidence2: "13"},
	{Type: 6, Scene: "深坞_冲刺能力旁", Evi: 1, Evidence1: "_", Evidence2: "14"},
	{Type: 6, Scene: "深坞_车站隐藏墙", Evi: 1, Evidence1: "_", Evidence2: "15"},
	{Type: 6, Scene: "深坞右下方隐藏房（需飞针）", Evi: 1, Evidence1: "_", Evidence2: "16"},
	{Type: 6, Scene: "远野左侧笼子", Evi: 1, Evidence1: "_", Evidence2: "17"},
	{Type: 6, Scene: "朝圣者憩所右侧门内(需从远野车站隐藏通道进入)", Evi: 1, Evidence1: "_", Evidence2: "18"},
	{Type: 6, Scene: "灰沼_腐囊虫庭附近", Evi: 1, Evidence1: "_", Evidence2: "19"},
	{Type: 6, Scene: "灰沼塔顶", Evi: 1, Evidence1: "_", Evidence2: "20"},
	{Type: 6, Scene: "灰沼_中途酒馆上方隐藏墙【色跳蚤】", Evi: 1, Evidence1: "_", Evidence2: "21"},
	{Type: 6, Scene: "甲木林拿螳螂爪路上", Evi: 1, Evidence1: "_", Evidence2: "22"},
	{Type: 6, Scene: "钟心镇上方钟道顶部", Evi: 1, Evidence1: "_", Evidence2: "23"},
	{Type: 6, Scene: "骸骨洞窟", Evi: 1, Evidence1: "_", Evidence2: "24"},
	{Type: 6, Scene: "猎人小径左侧（下劈红豆上去）", Evi: 1, Evidence1: "_", Evidence2: "25"},
	{Type: 6, Scene: "罪途左侧笼子", Evi: 1, Evidence1: "_", Evidence2: "26"},
	{Type: 6, Scene: "雪山跳蚤", Evi: 1, Evidence1: "_", Evidence2: "27"},
	{Type: 6, Scene: "圣堡工厂下层（全是炸弹人的房间）", Evi: 1, Evidence1: "_", Evidence2: "28"},
	{Type: 6, Scene: "圣堡工厂底部（火灵竹林出来）", Evi: 1, Evidence1: "_", Evidence2: "29"},
	{Type: 6, Scene: "蚀阶_车站左侧房间顶部", Evi: 1, Evidence1: "_", Evidence2: "30"},
	{Type: 6, Scene: "卡拉卡沙川_去往椅子路上", Evi: 1, Evidence1: "_", Evidence2: "31"},
	{Type: 6, Scene: "沙虫道_门上方隐藏墙", Evi: 1, Evidence1: "_", Evidence2: "32"},
	{Type: 6, Scene: "罪石监狱_小房间", Evi: 1, Evidence1: "_", Evidence2: "33"},
	{Type: 6, Scene: "罪石监狱_车站椅子上方", Evi: 1, Evidence1: "_", Evidence2: "34"},
	{Type: 6, Scene: "忆廊顶部【大跳蚤】", Evi: 1, Evidence1: "_", Evidence2: "35"},
	{Type: 6, Scene: "腐殖渠【龙牙跳蚤，救出可解锁全部跳蚤位置】", Evi: 1, Evidence1: "_", Evidence2: "36"},
	{Type: 6, Scene: "腐汁泽隐藏椅子上方跳蚤", Evi: 1, Evidence1: "_", Evidence2: "37"},
	{Type: 6, Scene: "腐汁泽下方隐藏墙", Evi: 1, Evidence1: "_", Evidence2: "38"},
	{Type: 6, Scene: "废旧管风琴（打完boss左走）", Evi: 1, Evidence1: "_", Evidence2: "39"},
	{Type: 6, Scene: "圣咏殿跳蚤（从餐厅往左走）", Evi: 1, Evidence1: "_", Evidence2: "40"},
	{Type: 6, Scene: "圣咏殿隐藏墙跳蚤（下方隐藏墙有风扇）", Evi: 1, Evidence1: "_", Evidence2: "41"},
	{Type: 6, Scene: "圣歌盟地右侧（需从图书馆隐藏墙上去）", Evi: 1, Evidence1: "_", Evidence2: "42"},
	{Type: 6, Scene: "图书馆推箱子", Evi: 1, Evidence1: "_", Evidence2: "43"},
}
