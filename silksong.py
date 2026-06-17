categories = ["能力", "法术", "纹章", "红色工具", "黄色工具", "蓝色工具", "面具碎片详情"]

# 工具
def get_tool(tool_name):
    def do_get_tool(d):
        for tool in d["playerData"]["Tools"]["savedData"]:
            if tool.get("Name") == tool_name:
                return tool.get("Data", {}).get("IsUnlocked", False)
        return False
    return do_get_tool

# 纹章
def get_tool_equips(tool_equips_name):
    def do_get_tool_equips(d):
        for tool in d["playerData"]["ToolEquips"]["savedData"]:
            if tool.get("Name") == tool_equips_name:
                return tool.get("Data", {}).get("IsUnlocked", False)
        return False
    return do_get_tool_equips

# 道具
def get_collectable_amount(collectable_name):
    def do_get_collectable_amount(d):
        for tool in d["playerData"]["Collectables"]["savedData"]:
            if tool.get("Name") == collectable_name:
                return tool.get("Data", {}).get("Amount", 0)
        return 0
    return do_get_collectable_amount

# name：显示名称
# category: 所属类别
# cur: 当前值，类型为一个函数 (d) => cur ，会将存档解析后的完整json格式传入d参数，可以返回一个数值，也可以返回bool值（表示已收集/未收集）
# total: 总值，不填则默认为1，可以填数字，也可以填上述 cur 字段的一个函数
items = [
    {
        "name": "罗盘",
        "category": "黄色工具",
        "cur": get_tool("Compass")
    },
    {
        "name": "碎壳坠",
        "category": "黄色工具",
        "cur": get_tool("Bone Necklace")
    },
    {
        "name": "磁石胸针",
        "category": "黄色工具",
        "cur": get_tool("Rosary Magnet")
    },
    {
        "name": "负重环带",
        "category": "黄色工具",
        "cur": get_tool("Weighted Anklet")
    },
    {
        "name": "棘刺手环",
        "category": "黄色工具",
        "cur": get_tool("Barbed Wire")
    },
    {
        "name": "亡虫囊/壳囊",
        "category": "黄色工具",
        "cur": lambda d: get_tool("Dead Mans Purse")(d) or get_tool("Shell Satchel")(d)
    },
    {
        "name": "磁石骰",
        "category": "黄色工具",
        "cur": get_tool("Magnetite Dice")
    },
    {
        "name": "迅捷脊锁",
        "category": "黄色工具",
        "cur": get_tool("Scuttlebrace")
    },
    {
        "name": "登极握爪",
        "category": "黄色工具",
        "cur": get_tool("Wallcling")
    },
    {
        "name": "蛛丝弦",
        "category": "黄色工具",
        "cur": get_tool("Musician Charm")
    },
    {
        "name": "丝速脚环",
        "category": "黄色工具",
        "cur": get_tool("Sprintmaster")
    },
    {
        "name": "窃者印记",
        "category": "黄色工具",
        "cur": get_tool("Thief Charm")
    },
    {
        "name": "直针",
        "category": "红色工具",
        "cur": get_tool("Straight Pin")
    },
    {
        "name": "三重镖",
        "category": "红色工具",
        "cur": get_tool("Tri Pin")
    },
    {
        "name": "蛰刺碎片",
        "category": "红色工具",
        "cur": get_tool("Sting Shard")
    },
    {
        "name": "钉刺",
        "category": "红色工具",
        "cur": get_tool("Tack")
    },
    {
        "name": "长针",
        "category": "红色工具",
        "cur": get_tool("Harpoon")
    },
    {
        "name": "弧爪/曲镰",
        "category": "红色工具",
        "cur": lambda d: get_tool("Curve Claws")(d) or get_tool("Curve Claws Upgraded")(d)
    },
    {
        "name": "投掷环",
        "category": "红色工具",
        "cur": get_tool("Shakra Ring")
    },
    {
        "name": "爆燃囊",
        "category": "红色工具",
        "cur": get_tool("Pimpilo")
    },
    {
        "name": "螺切刃",
        "category": "红色工具",
        "cur": get_tool("Conch Drill")
    },
    {
        "name": "丝弹（三选一）",
        "category": "红色工具",
        "cur": lambda d: get_tool("WebShot Weaver")(d) or get_tool("WebShot Architect")(d) or get_tool("WebShot Forge")(d)
    },
    {
        "name": "掘洞钻",
        "category": "红色工具",
        "cur": get_tool("Screw Attack")
    },
    {
        "name": "机轮刃",
        "category": "红色工具",
        "cur": get_tool("Cogwork Saw")
    },
    {
        "name": "齿轮蜂",
        "category": "红色工具",
        "cur": get_tool("Cogwork Flier")
    },
    {
        "name": "念珠炮",
        "category": "红色工具",
        "cur": get_tool("Rosary Cannon")
    },
    {
        "name": "电枢球",
        "category": "红色工具",
        "cur": get_tool("Lightning Rod")
    },
    {
        "name": "燧石板",
        "category": "红色工具",
        "cur": get_tool("Flintstone")
    },
    {
        "name": "跳蚤秘酿",
        "category": "红色工具",
        "cur": get_tool("Flea Brew")
    },
    {
        "name": "生质液瓶",
        "category": "红色工具",
        "cur": get_tool("Lifeblood Syringe")
    },
    {
        "name": "德鲁伊之眼/德鲁伊双瞳",
        "category": "蓝色工具",
        "cur": lambda d: get_tool("Mosscreep Tool 1")(d) or get_tool("Mosscreep Tool 2")(d)
    },
    {
        "name": "熔岩钟",
        "category": "蓝色工具",
        "cur": get_tool("Lava Charm")
    },
    {
        "name": "护佑钟",
        "category": "蓝色工具",
        "cur": get_tool("Bell Bind")
    },
    {
        "name": "花芯囊",
        "category": "蓝色工具",
        "cur": get_tool("Poison Pouch")
    },
    {
        "name": "碎面甲",
        "category": "蓝色工具",
        "cur": get_tool("Fractured Mask")
    },
    {
        "name": "多重缚丝器",
        "category": "蓝色工具",
        "cur": get_tool("Multibind")
    },
    {
        "name": "织光仪",
        "category": "蓝色工具",
        "cur": get_tool("White Ring")
    },
    {
        "name": "锯齿环",
        "category": "蓝色工具",
        "cur": get_tool("Brolly Spike")
    },
    {
        "name": "注丝套针",
        "category": "蓝色工具",
        "cur": get_tool("Quickbind")
    },
    {
        "name": "储丝延展器",
        "category": "蓝色工具",
        "cur": get_tool("Spool Extender")
    },
    {
        "name": "储备缚丝",
        "category": "蓝色工具",
        "cur": get_tool("Reserve Bind")
    },
    {
        "name": "爪镜/双生爪镜",
        "category": "蓝色工具",
        "cur": lambda d: get_tool("Dazzle Bind")(d) or get_tool("Dazzle Bind Upgraded")(d)
    },
    {
        "name": "记忆晶石",
        "category": "蓝色工具",
        "cur": get_tool("Revenge Crystal")
    },
    {
        "name": "撬赃钩",
        "category": "蓝色工具",
        "cur": get_tool("Thief Claw")
    },
    {
        "name": "伏特丝",
        "category": "蓝色工具",
        "cur": get_tool("Zap Imbuement")
    },
    {
        "name": "速射索",
        "category": "蓝色工具",
        "cur": get_tool("Quick Sling")
    },
    {
        "name": "净界花环",
        "category": "蓝色工具",
        "cur": get_tool("Maggot Charm")
    },
    {
        "name": "长爪",
        "category": "蓝色工具",
        "cur": get_tool("Longneedle")
    },
    {
        "name": "灵火提灯",
        "category": "蓝色工具",
        "cur": get_tool("Wisp Lantern")
    },
    {
        "name": "蚤母卵",
        "category": "蓝色工具",
        "cur": get_tool("Flea Charm")
    },
    {
        "name": "针徽",
        "category": "蓝色工具",
        "cur": get_tool("Pinstress Tool")
    },
    {
        "name": "工具袋升级",
        "category": "能力",
        "cur": lambda d: d["playerData"].get("ToolPouchUpgrades", 0),
        "total": 4
    },
    {
        "name": "制作匣升级",
        "category": "能力",
        "cur": lambda d: d["playerData"].get("ToolKitUpgrades", 0),
        "total": 4
    },
    {
        "name": "丝之矛",
        "category": "法术",
        "cur": get_tool("Silk Spear")
    },
    {
        "name": "灵丝风暴",
        "category": "法术",
        "cur": get_tool("Thread Sphere")
    },
    {
        "name": "十字绣",
        "category": "法术",
        "cur": get_tool("Parry")
    },
    {
        "name": "丝刃镖",
        "category": "法术",
        "cur": get_tool("Silk Charge")
    },
    {
        "name": "符文之怒",
        "category": "法术",
        "cur": get_tool("Silk Bomb")
    },
    {
        "name": "苍白之爪",
        "category": "法术",
        "cur": get_tool("Silk Boss Needle")
    },
    {
        "name": "丝之心",
        "category": "能力",
        "cur": lambda d: d["playerData"]["silkRegenMax"],
        "total": 3
    },
    {
        "name": "收割者纹章",
        "category": "纹章",
        "cur": get_tool_equips("Reaper"),
    },
    {
        "name": "漫游者纹章",
        "category": "纹章",
        "cur": get_tool_equips("Wanderer"),
    },
    {
        "name": "野兽纹章",
        "category": "纹章",
        "cur": get_tool_equips("Warrior"),
    },
    {
        "name": "建筑师纹章",
        "category": "纹章",
        "cur": get_tool_equips("Toolmaster"),
    },
    {
        "name": "巫妪纹章",
        "category": "纹章",
        "cur": get_tool_equips("Witch"),
    },
    {
        "name": "萨满纹章",
        "category": "纹章",
        "cur": get_tool_equips("Spell"),
    },
    {
        "name": "疾风步",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasDash"]
    },
    {
        "name": "蛛攀术",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasWalljump"]
    },
    {
        "name": "飞针冲刺",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasHarpoonDash"]
    },
    {
        "name": "灵丝升腾",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasSuperJump"]
    },
    {
        "name": "蓄力斩",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasChargeSlash"]
    },
    {
        "name": "织忆弦针",
        "category": "能力",
        "cur": lambda d: d["playerData"]["hasNeedolin"]
    },
    {
        "name": "风铃瑶",
        "category": "能力",
        "cur": lambda d: d["playerData"]["HasBoundCrestUpgrader"]
    },
    {
        "name": "面具",
        "category": "能力",
        "cur": lambda d: d["playerData"]["maxHealthBase"] - 5,
        "total": 5
    },
    {
        "name": "灵丝轴",
        "category": "能力",
        "cur": lambda d: d["playerData"]["silkMax"] - 9,
        "total": 9
    },
    {
        "name": "织针磨砺",
        "category": "能力",
        "cur": lambda d: d["playerData"]["nailUpgrades"],
        "total": 4
    },
    {
        "name": "永绽花",
        "category": "能力",
        "cur": get_collectable_amount("White Flower")
    },
]

def get_question_complete(question_name):
    def do_get_question_complete(d):
        for tool in d["playerData"]["QuestCompletionData"]["savedData"]:
            if tool.get("Name") == question_name:
                return tool.get("Data", {}).get("IsCompleted", False)
        return False
    return do_get_question_complete

# 字段结构同 items ，但不计入完成度
other_items = [
    {
        "name": "骸底镇商店",
        "category": "面具碎片详情",
        "cur": lambda d: d["playerData"].get("PurchasedBonebottomHeartPiece", False)
    },
    {
        "name": "圣歌盟地商店",
        "category": "面具碎片详情",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveShellFragment", False)
    },
    {
        "name": "暴怒兽蝇祈愿",
        "category": "面具碎片详情",
        "cur": get_question_complete("Beastfly Hunt")
    },
    {
        "name": "隐秘猎手祈愿",
        "category": "面具碎片详情",
        "cur": get_question_complete("Ant Trapper")
    },
    {
        "name": "竞速冠军祈愿",
        "category": "面具碎片详情",
        "cur": get_question_complete("Sprintmaster Race")
    },
    {
        "name": "暗蚀之心祈愿",
        "category": "面具碎片详情",
        "cur": get_question_complete("Black Thread Pt5 Heart")
    },
]