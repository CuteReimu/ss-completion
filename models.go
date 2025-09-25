package main

import (
	"encoding/json"
	"fmt"
)

// CheckItem 检查项结构
type CheckItem struct {
	CheckId   int    `json:"checkId"`
	Type      int    `json:"type"`
	Scene     string `json:"scene"`
	Evi       int    `json:"evi"`
	Evidence1 string `json:"evidence1"`
	Evidence2 string `json:"evidence2"`
	Axis      string `json:"axis"`
}

// HiData 结果数据结构
type HiData struct {
	CheckId int    `json:"checkId"`
	Scene   string `json:"scene"`
	Axis    string `json:"axis"`
	ResStr  string `json:"resStr"`
}

// HiResult 分析结果
type HiResult struct {
	BoxList   []*HiData
	HeartList []*HiData
	MetalList []*HiData
	SilkList  []*HiData
}

// PlayerData 玩家数据结构
type PlayerData struct {
	PurchasedBonebottomHeartPiece     bool `json:"PurchasedBonebottomHeartPiece"`
	PurchasedBonebottomToolMetal      bool `json:"PurchasedBonebottomToolMetal"`
	PurchasedPilgrimsRestMemoryLocket bool `json:"PurchasedPilgrimsRestMemoryLocket"`
	PurchasedBelltownMemoryLocket     bool `json:"PurchasedBelltownMemoryLocket"`
	PurchasedBelltownSpoolSegment     bool `json:"PurchasedBelltownSpoolSegment"`
	MerchantEnclaveShellFragment      bool `json:"MerchantEnclaveShellFragment"`
	PurchasedGrindleSpoolPiece        bool `json:"PurchasedGrindleSpoolPiece"`
	MetCaravanTroupeLeaderJudge       bool `json:"MetCaravanTroupeLeaderJudge"`
	MerchantEnclaveToolMetal          bool `json:"MerchantEnclaveToolMetal"`
	MerchantEnclaveSpoolPiece         bool `json:"MerchantEnclaveSpoolPiece"`
}

// 检查项数据
var checkItems []CheckItem

// init 初始化检查项数据
func init() {
	checkData := `[{"checkId":1,"type":4,"scene":"骸骨洞窟","evi":0,"evidence1":"Bone_07","evidence2":"Collectable Item Pickup - Tool Metal","axis":"Bone_07(37,5)"},{"checkId":2,"type":4,"scene":"深坞右侧宝箱","evi":0,"evidence1":"Dock_03","evidence2":"Collectable Item Pickup","axis":"Dock_03(11,82)"},{"checkId":3,"type":3,"scene":"猎人小径野兽教堂旁","evi":0,"evidence1":"Ant_20","evidence2":"Collectable Item Pickup","axis":"Ant_20(145,12)"},{"checkId":4,"type":0,"scene":"远野炸地板","evi":0,"evidence1":"Bone_East_20","evidence2":"Heart Piece","axis":"Bone_East_20(92,17)"},{"checkId":5,"type":0,"scene":"骸底买面具","evi":1,"evidence1":"Bonetown","evidence2":"1","axis":"商店购买"},{"checkId":6,"type":4,"scene":"骸底买金属","evi":1,"evidence1":"Bonetown","evidence2":"2","axis":"商店购买"},{"checkId":7,"type":0,"scene":"沙虫道","evi":0,"evidence1":"Crawl_02","evidence2":"Heart Piece","axis":"Crawl_02(22,5)"},{"checkId":8,"type":3,"scene":"朝圣者憩所购买","evi":1,"evidence1":"Bone_East_10_Room","evidence2":"3","axis":"商店购买"},{"checkId":9,"type":0,"scene":"甲木林","evi":0,"evidence1":"Crawl_02","evidence2":"Heart Piece","axis":"Shellwood_14(128,12)"},{"checkId":10,"type":3,"scene":"骸骨洞窟","evi":0,"evidence1":"Bone_18","evidence2":"Collectable Item Pickup","axis":"Bone_18(36,22)"},{"checkId":11,"type":0,"scene":"洞窟与深坞之间","evi":0,"evidence1":"Dock_08","evidence2":"Heart Piece","axis":"Dock_08(54,20)"},{"checkId":12,"type":3,"scene":"骸底提交暴烈燧甲虫任务","evi":2,"evidence1":"Bonetown","evidence2":"Rock Rollers","axis":"任务提交"},{"checkId":13,"type":1,"scene":"出生点织巢","evi":0,"evidence1":"Weave_11","evidence2":"Silk Spool","axis":"Weave_11(15,24)"},{"checkId":14,"type":3,"scene":"钟心镇购买盒子","evi":1,"evidence1":"Belltown","evidence2":"4","axis":"商店购买"},{"checkId":15,"type":3,"scene":"工厂忏悔机旁光源","evi":0,"evidence1":"Under_08","evidence2":"Collectable Item Pickup","axis":"Under_08(61,18)"},{"checkId":16,"type":1,"scene":"圣煲工厂","evi":0,"evidence1":"Under_10","evidence2":"Silk Spool","axis":"Under_10(22,6)"},{"checkId":17,"type":1,"scene":"圣扉巨门顶部","evi":0,"evidence1":"Song_19_entrance","evidence2":"Silk Spool","axis":"Song_19_entrance(22,94)"},{"checkId":18,"type":3,"scene":"圣煲钟道顶部","evi":0,"evidence1":"Bellway_City","evidence2":"Collectable Item Pickup","axis":"Bellway_City(68,26)"},{"checkId":19,"type":1,"scene":"圣煲工厂底部","evi":0,"evidence1":"Library_11b","evidence2":"Silk Spool","axis":"Library_11b(22,7)"},{"checkId":20,"type":4,"scene":"圣煲工厂","evi":0,"evidence1":"Under_19b","evidence2":"Collectable Item Pickup - Tool Metal","axis":"Under_19b(10,7)"},{"checkId":21,"type":1,"scene":"灰沼顶部","evi":0,"evidence1":"Greymoor_02","evidence2":"Silk Spool","axis":"Greymoor_02(30,137)"},{"checkId":22,"type":1,"scene":"白愈厅救谢尔玛","evi":0,"evidence1":"Ward_09","evidence2":"ward_junk_pile_break","axis":"商店购买"},{"checkId":23,"type":1,"scene":"白愈厅电梯下方","evi":0,"evidence1":"Ward_01","evidence2":"Silk Spool","axis":"Ward_01(29,6)"},{"checkId":24,"type":1,"scene":"钟心镇买丝轴","evi":1,"evidence1":"Belltown","evidence2":"5","axis":"商店购买"},{"checkId":25,"type":0,"scene":"圣歌盟地买面具","evi":1,"evidence1":"Song_Enclave","evidence2":"6","axis":"商店购买"},{"checkId":26,"type":0,"scene":"火灵竹林","evi":0,"evidence1":"Wisp_07","evidence2":"Heart Piece","axis":"Wisp_07(251,24)"},{"checkId":27,"type":4,"scene":"火灵竹林","evi":0,"evidence1":"Wisp_05","evidence2":"Collectable Item Pickup - Tool Metal","axis":"Wisp_05(42,58)"},{"checkId":28,"type":1,"scene":"忆廊","evi":0,"evidence1":"Arborium_09","evidence2":"Silk Spool","axis":"Arborium_09(19,32)"},{"checkId":29,"type":3,"scene":"忆廊","evi":0,"evidence1":"Arborium_05","evidence2":"Collectable Item Pickup","axis":"Arborium_05(5,9)"},{"checkId":30,"type":4,"scene":"腐殖渠","evi":0,"evidence1":"Aqueduct_05","evidence2":"Collectable Item Pickup - Tool Metal","axis":"Aqueduct_05(325,17)"},{"checkId":31,"type":0,"scene":"远野岩浆挑战","evi":0,"evidence1":"Bone_East_LavaChallenge","evidence2":"Heart Piece (1)","axis":"Bone_East_LavaChallenge(21,278)"},{"checkId":32,"type":3,"scene":"腐汁泽左上角","evi":0,"evidence1":"Shadow_20","evidence2":"Collectable Item Pickup","axis":"Shadow_20(18,25)"},{"checkId":33,"type":3,"scene":"腐汁泽打沙包","evi":0,"evidence1":"Shadow_27","evidence2":"Sack Corpse Pickup","axis":"Shadow_27(192,10)"},{"checkId":34,"type":0,"scene":"腐汁泽","evi":0,"evidence1":"Shadow_13","evidence2":"Heart Piece","axis":"Shadow_13(308,63)"},{"checkId":35,"type":3,"scene":"中途酒馆","evi":0,"evidence1":"Halfway_01","evidence2":"Collectable Item Pickup","axis":"Halfway_01(9,15)"},{"checkId":36,"type":1,"scene":"蚀阶小偷购买","evi":1,"evidence1":"Coral_42","evidence2":"7","axis":"商店购买"},{"checkId":37,"type":3,"scene":"卡拉卡沙川","evi":0,"evidence1":"Coral_23","evidence2":"Collectable Item Pickup","axis":"Coral_23(91,52)"},{"checkId":38,"type":4,"scene":"蚀阶","evi":0,"evidence1":"Coral_32","evidence2":"Collectable Item Pickup - Tool Metal","axis":"Coral_32(78,9)"},{"checkId":39,"type":1,"scene":"解救14只跳蚤","evi":1,"evidence1":"Coral_Judge_Arena","evidence2":"8","axis":"商店购买"},{"checkId":40,"type":3,"scene":"灰沼车站左侧","evi":0,"evidence1":"Greymoor_16","evidence2":"Collectable Item Pickup","axis":"Greymoor_16(131,53)"},{"checkId":41,"type":0,"scene":"机枢核心左边","evi":0,"evidence1":"Song_09","evidence2":"Heart Piece","axis":"Song_09(42,43)"},{"checkId":42,"type":0,"scene":"出生点织巢","evi":0,"evidence1":"Weave_05b","evidence2":"Heart Piece","axis":"Weave_05b(161,29)"},{"checkId":43,"type":0,"scene":"钟心镇猎杀兽蝇任务","evi":2,"evidence1":"Belltown","evidence2":"Beastfly Hunt","axis":"任务提交"},{"checkId":44,"type":0,"scene":"图书馆玻璃罐","evi":0,"evidence1":"Library_05","evidence2":"library_glass_heart_piece","axis":"Library_05(17,70)"},{"checkId":45,"type":1,"scene":"高庭顶部","evi":0,"evidence1":"Hang_03_top","evidence2":"Silk Spool","axis":"Hang_03_top(18,156)"},{"checkId":46,"type":4,"scene":"圣歌盟地买金属","evi":1,"evidence1":"Song_Enclave","evidence2":"9","axis":"商店购买"},{"checkId":47,"type":1,"scene":"圣歌盟地买丝轴","evi":1,"evidence1":"Song_Enclave","evidence2":"10","axis":"商店购买"},{"checkId":48,"type":0,"scene":"罪石监狱上右","evi":0,"evidence1":"Slab_17","evidence2":"Heart Piece","axis":"Slab_17(19,68)"},{"checkId":49,"type":1,"scene":"罪石监狱左侧","evi":0,"evidence1":"Peak_01","evidence2":"Silk Spool","axis":"Peak_01(86,192)"},{"checkId":50,"type":0,"scene":"雪山柱子内","evi":0,"evidence1":"Peak_04c","evidence2":"Heart Piece","axis":"Peak_04c(68,8)"},{"checkId":51,"type":0,"scene":"蚀阶","evi":0,"evidence1":"Peak_04c","evidence2":"Heart Piece","axis":"Coral_19b(75,108)"},{"checkId":52,"type":1,"scene":"深坞","evi":0,"evidence1":"Bone_East_13","evidence2":"Silk Spool","axis":"Bone_East_13(41,24)"},{"checkId":53,"type":1,"scene":"德鲁伊下方","evi":0,"evidence1":"Bone_11b","evidence2":"Silk Spool","axis":"Bone_11b(31,5)"},{"checkId":54,"type":1,"scene":"深坞右侧","evi":0,"evidence1":"Dock_03c","evidence2":"Silk Spool","axis":"Dock_03c(128,55)"},{"checkId":55,"type":1,"scene":"机枢核心右下","evi":0,"evidence1":"Cog_07","evidence2":"Silk Spool","axis":"Cog_07(83,15)"},{"checkId":56,"type":3,"scene":"沙虫道左下","evi":0,"evidence1":"Crawl_09","evidence2":"Collectable Item Pickup","axis":"Crawl_09(130,5)"},{"checkId":57,"type":3,"scene":"蚀阶","evi":0,"evidence1":"Coral_02","evidence2":"Collectable Item Pickup (1)","axis":"Coral_02(202,45)"},{"checkId":58,"type":3,"scene":"图书馆右上","evi":0,"evidence1":"Library_08","evidence2":"Collectable Item Pickup","axis":"Library_08(106,35)"},{"checkId":59,"type":3,"scene":"深坞温泉房下方","evi":0,"evidence1":"Dock_13","evidence2":"Collectable Item Pickup","axis":"Dock_13(15,5)"},{"checkId":60,"type":3,"scene":"罪石监狱","evi":0,"evidence1":"Slab_Cell_Quiet","evidence2":"Collectable Item Pickup","axis":"Slab_Cell_Quiet(43,32)"},{"checkId":61,"type":3,"scene":"第三幕远野右上方","evi":0,"evidence1":"Bone_East_25","evidence2":"Collectable Item Pickup","axis":"Bone_East_25(152,8)"},{"checkId":62,"type":0,"scene":"第三幕飞毛腿赛跑","evi":2,"evidence1":"Sprintmaster_Cave","evidence2":"Sprintmaster Race","axis":"Sprintmaster_Cave(50,14)"},{"checkId":63,"type":3,"scene":"第三幕钟心镇上冲","evi":0,"evidence1":"Belltown","evidence2":"Collectable Item Pickup","axis":"Belltown(59,68)"},{"checkId":64,"type":0,"scene":"第三幕雪山洞窟","evi":0,"evidence1":"Peak_06","evidence2":"Heart Piece","axis":"Peak_06(28,182)"},{"checkId":65,"type":0,"scene":"第三幕暗蚀之心任务","evi":2,"evidence1":"Belltown","evidence2":"Destroy Thread Cores","axis":"任务提交"},{"checkId":66,"type":0,"scene":"第三幕隐秘猎手任务","evi":2,"evidence1":"Belltown","evidence2":"Ant Trapper","axis":"任务提交"}]`

	if err := json.Unmarshal([]byte(checkData), &checkItems); err != nil {
		panic(fmt.Sprintf("Failed to load check data: %v", err))
	}
}
