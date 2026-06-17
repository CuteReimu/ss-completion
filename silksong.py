# 所有类别的列表，最终会按照这个列表进行排序
categories = ["红色工具", "蓝色工具", "黄色工具", "法术", "纹章", "能力", "其它", "面具碎片详情", "灵丝轴碎片详情", "跳蚤", "制造金属", "忆境纪念盒（不计完成度）", "苔莓（不占完成度）"]

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
# total: 总值，不填则默认为1
# icon: 图标，填写一个url，可以不填
# wiki: Wiki链接，填写一个url，可以不填
# desc: 简介，鼠标放上去弹出的tooltip，可以不填
items = [
    {
        "name": "罗盘",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/92/Compass.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/罗盘",
        "cur": get_tool("Compass")
    },
    {
        "name": "碎壳坠",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/f2/Shard_Pendant.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/碎壳坠",
        "cur": get_tool("Bone Necklace")
    },
    {
        "name": "磁石胸针",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/22/Magnetite_Brooch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/磁石胸针",
        "cur": get_tool("Rosary Magnet")
    },
    {
        "name": "负重环带",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ee/Weighted_Belt.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/负重环带",
        "cur": get_tool("Weighted Anklet")
    },
    {
        "name": "棘刺手环",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5e/Barbed_Bracelet.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/棘刺手环",
        "cur": get_tool("Barbed Wire")
    },
    {
        "name": "亡虫囊/壳囊",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fc/Dead_Bug%27s_Purse.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/亡虫囊",
        "cur": lambda d: get_tool("Dead Mans Purse")(d) or get_tool("Shell Satchel")(d)
    },
    {
        "name": "磁石骰",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/3a/Magnetite_Dice.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/磁石骰",
        "cur": get_tool("Magnetite Dice")
    },
    {
        "name": "迅捷脊锁",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/05/Scuttlebrace.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/迅捷脊锁",
        "cur": get_tool("Scuttlebrace")
    },
    {
        "name": "登极握爪",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fe/Ascendants_Grip.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/登极握爪",
        "cur": get_tool("Wallcling")
    },
    {
        "name": "蛛丝弦",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/bf/Spider_Strings.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛛丝弦",
        "cur": get_tool("Musician Charm")
    },
    {
        "name": "丝速脚环",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/b3/Silkspeed_Anklets.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝速脚环",
        "cur": get_tool("Sprintmaster")
    },
    {
        "name": "窃者印记",
        "category": "黄色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/80/Thiefs_Mark.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/窃者印记",
        "cur": get_tool("Thief Charm")
    },
    {
        "name": "直针",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/03/Straight_Pin.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/直针",
        "cur": get_tool("Straight Pin")
    },
    {
        "name": "三重镖",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a6/Tri-Pins.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/三重镖",
        "cur": get_tool("Tri Pin")
    },
    {
        "name": "蛰刺碎片",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/69/Sting_Shard.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛰刺碎片",
        "cur": get_tool("Sting Shard")
    },
    {
        "name": "钉刺",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ef/Tacks.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/钉刺",
        "cur": get_tool("Tack")
    },
    {
        "name": "长针",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/cb/Longpin.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/长针",
        "cur": get_tool("Harpoon")
    },
    {
        "name": "弧爪/曲镰",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/20/Curveclaw.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/弧爪",
        "cur": lambda d: get_tool("Curve Claws")(d) or get_tool("Curve Claws Upgraded")(d)
    },
    {
        "name": "投掷环",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2b/Throwing_Ring.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/投掷环",
        "cur": get_tool("Shakra Ring")
    },
    {
        "name": "爆燃囊",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/b0/Pimpillo.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/爆燃囊",
        "cur": get_tool("Pimpilo")
    },
    {
        "name": "螺切刃",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0f/Conchcutter.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/螺切刃",
        "cur": get_tool("Conch Drill")
    },
    {
        "name": "丝弹（三选一）",
        "category": "红色工具",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/b3/Silkshot.png/72px-Silkshot.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝弹",
        "cur": lambda d: get_tool("WebShot Weaver")(d) or get_tool("WebShot Architect")(d) or get_tool("WebShot Forge")(d)
    },
    {
        "name": "掘洞钻",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/59/Delvers_Drill.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/掘洞钻",
        "cur": get_tool("Screw Attack")
    },
    {
        "name": "机轮刃",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8e/Cogwork_Wheel.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/机轮刃",
        "cur": get_tool("Cogwork Saw")
    },
    {
        "name": "齿轮蜂",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/ba/Cogfly.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/齿轮蜂",
        "cur": get_tool("Cogwork Flier")
    },
    {
        "name": "念珠炮",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/25/Rosary_Cannon_Loaded.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/念珠炮",
        "cur": get_tool("Rosary Cannon")
    },
    {
        "name": "电枢球",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/75/Voltvessels.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/电枢球",
        "cur": get_tool("Lightning Rod")
    },
    {
        "name": "燧石板",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/37/Flintslate.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/燧石板",
        "cur": get_tool("Flintstone")
    },
    {
        "name": "跳蚤秘酿",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d0/Flea_Brew.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/跳蚤秘酿",
        "cur": get_tool("Flea Brew")
    },
    {
        "name": "生质液瓶",
        "category": "红色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/Plasmium_Phial.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/生质液瓶",
        "cur": get_tool("Lifeblood Syringe")
    },
    {
        "name": "德鲁伊之眼/德鲁伊双瞳",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/13/Druid%27s_Eye.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/德鲁伊之眼",
        "cur": lambda d: get_tool("Mosscreep Tool 1")(d) or get_tool("Mosscreep Tool 2")(d)
    },
    {
        "name": "熔岩钟",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/72/Magma_Bell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/熔岩钟",
        "cur": get_tool("Lava Charm")
    },
    {
        "name": "护佑钟",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8c/Warding_Bell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/护佑钟",
        "cur": get_tool("Bell Bind")
    },
    {
        "name": "花芯囊",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/Pollip_Pouch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/花芯囊",
        "cur": get_tool("Poison Pouch")
    },
    {
        "name": "碎面甲",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/51/Fractured_Mask.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/碎面甲",
        "cur": get_tool("Fractured Mask")
    },
    {
        "name": "多重缚丝器",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/19/Multibinder.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/多重缚丝器",
        "cur": get_tool("Multibind")
    },
    {
        "name": "织光仪",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5f/Weavelight.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织光仪",
        "cur": get_tool("White Ring")
    },
    {
        "name": "锯齿环",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/45/Sawtooth_Circlet.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/锯齿环",
        "cur": get_tool("Brolly Spike")
    },
    {
        "name": "注丝套针",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/dd/Injector_Band.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/注丝套针",
        "cur": get_tool("Quickbind")
    },
    {
        "name": "储丝延展器",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/17/Spool_Extender.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/储丝延展器",
        "cur": get_tool("Spool Extender")
    },
    {
        "name": "储备缚丝",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/13/Reserve_Bind.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/储备缚丝",
        "cur": get_tool("Reserve Bind")
    },
    {
        "name": "爪镜/双生爪镜",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fe/Claw_Mirror.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/爪镜",
        "cur": lambda d: get_tool("Dazzle Bind")(d) or get_tool("Dazzle Bind Upgraded")(d)
    },
    {
        "name": "记忆晶石",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/6b/Memory_Crystal.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/记忆晶石",
        "cur": get_tool("Revenge Crystal")
    },
    {
        "name": "撬赃钩",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/eb/Snitch_Pick.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/撬赃钩",
        "cur": get_tool("Thief Claw")
    },
    {
        "name": "伏特丝",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c4/Volt_Filament.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/伏特丝",
        "cur": get_tool("Zap Imbuement")
    },
    {
        "name": "速射索",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/4a/Quick_Sling.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/速射索",
        "cur": get_tool("Quick Sling")
    },
    {
        "name": "净界花环",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c2/Wreath_of_Purity.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/净界花环",
        "cur": get_tool("Maggot Charm")
    },
    {
        "name": "长爪",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/73/Longclaw.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/长爪",
        "cur": get_tool("Longneedle")
    },
    {
        "name": "灵火提灯",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/80/Wispfire_Lantern.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵火提灯",
        "cur": get_tool("Wisp Lantern")
    },
    {
        "name": "蚤母卵",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a4/Egg_of_Flealia.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蚤母卵",
        "cur": get_tool("Flea Charm")
    },
    {
        "name": "针徽",
        "category": "蓝色工具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/50/Pin_Badge.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/针徽",
        "cur": get_tool("Pinstress Tool")
    },
    {
        "name": "工具袋升级",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e9/Tool_Pouch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/工具袋",
        "cur": lambda d: d["playerData"].get("ToolPouchUpgrades", 0),
        "total": 4
    },
    {
        "name": "制作匣升级",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5d/Crafting_Kit.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/制作匣",
        "cur": lambda d: d["playerData"].get("ToolKitUpgrades", 0),
        "total": 4
    },
    {
        "name": "丝之矛",
        "category": "法术",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/a/a4/Icon_SS_Silkspear.png/438px-Icon_SS_Silkspear.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝之矛",
        "cur": get_tool("Silk Spear")
    },
    {
        "name": "灵丝风暴",
        "category": "法术",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8c/Icon_SS_Thread_Storm.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵丝风暴",
        "cur": get_tool("Thread Sphere")
    },
    {
        "name": "十字绣",
        "category": "法术",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/2/25/Icon_SS_Cross_Stitch.png/438px-Icon_SS_Cross_Stitch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/十字绣",
        "cur": get_tool("Parry")
    },
    {
        "name": "丝刃镖",
        "category": "法术",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/87/Icon_SS_Sharpdart.png/438px-Icon_SS_Sharpdart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝刃镖",
        "cur": get_tool("Silk Charge")
    },
    {
        "name": "符文之怒",
        "category": "法术",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/9/91/Icon_SS_Rune_Rage.png/438px-Icon_SS_Rune_Rage.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/符文之怒",
        "cur": get_tool("Silk Bomb")
    },
    {
        "name": "苍白之爪",
        "category": "法术",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d9/Icon_SS_Pale_Nails.png/408px-Icon_SS_Pale_Nails.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/苍白之爪",
        "cur": get_tool("Silk Boss Needle")
    },
    {
        "name": "丝之心",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/de/Icon_SS_Silk_Heart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝之心",
        "cur": lambda d: d["playerData"]["silkRegenMax"],
        "total": 3
    },
    {
        "name": "收割者纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/0/0c/Reaper_Crest_Inventory.png/438px-Reaper_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/收割者纹章",
        "cur": get_tool_equips("Reaper"),
    },
    {
        "name": "漫游者纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/5/5e/Wanderer_Crest_Inventory.png/322px-Wanderer_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/漫游者纹章",
        "cur": get_tool_equips("Wanderer"),
    },
    {
        "name": "野兽纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/b9/Beast_Crest_Inventory.png/438px-Beast_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/野兽纹章",
        "cur": get_tool_equips("Warrior"),
    },
    {
        "name": "建筑师纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d4/Architect_Crest_Inventory.png/412px-Architect_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/建筑师纹章",
        "cur": get_tool_equips("Toolmaster"),
    },
    {
        "name": "巫妪纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d0/Witch_Crest_Inventory.png/426px-Witch_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/巫妪纹章",
        "cur": get_tool_equips("Witch"),
    },
    {
        "name": "萨满纹章",
        "category": "纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d8/Shaman_Crest_Inventory.png/435px-Shaman_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/萨满纹章",
        "cur": get_tool_equips("Spell"),
    },
    {
        "name": "疾风步",
        "category": "能力",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/f/f2/Icon_SS_Swift_Step_Art.png/438px-Icon_SS_Swift_Step_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/疾风步",
        "cur": lambda d: d["playerData"]["hasDash"]
    },
    {
        "name": "蛛攀术",
        "category": "能力",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/3/3b/Icon_SS_Cling_Grip_Art.png/357px-Icon_SS_Cling_Grip_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛛攀术",
        "cur": lambda d: d["playerData"]["hasWalljump"]
    },
    {
        "name": "飞针冲刺",
        "category": "能力",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/6/6f/Icon_SS_Clawline_Art.png/438px-Icon_SS_Clawline_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/飞针冲刺",
        "cur": lambda d: d["playerData"]["hasHarpoonDash"]
    },
    {
        "name": "灵丝升腾",
        "category": "能力",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e8/Icon_SS_Silk_Soar_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵丝升腾",
        "cur": lambda d: d["playerData"]["hasSuperJump"]
    },
    {
        "name": "蓄力斩",
        "category": "能力",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/8e/Icon_SS_Needle_Strike_Art.png/438px-Icon_SS_Needle_Strike_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蓄力斩",
        "cur": lambda d: d["playerData"]["hasChargeSlash"]
    },
    {
        "name": "织忆弦针",
        "category": "能力",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c0/Icon_SS_Needolin_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织忆弦针",
        "cur": lambda d: d["playerData"]["hasNeedolin"]
    },
    {
        "name": "风铃瑶",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/0/00/Icon_SS_Sylphsong_Art.png/438px-Icon_SS_Sylphsong_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/%E9%A3%8E%E7%81%B5%E8%B0%A3",
        "cur": lambda d: d["playerData"]["HasBoundCrestUpgrader"]
    },
    {
        "name": "面具",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/9/91/SS_Mask.png/50px-SS_Mask.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/面具碎片_(丝之歌)",
        "cur": lambda d: d["playerData"]["maxHealthBase"] - 5,
        "total": 5
    },
    {
        "name": "灵丝",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/83/Silk.png/80px-Silk.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵丝轴碎片",
        "cur": lambda d: d["playerData"]["silkMax"] - 9,
        "total": 9
    },
    {
        "name": "织针磨砺",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/87/Needle_2_Sharpened_Needle.png/54px-Needle_2_Sharpened_Needle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织针",
        "cur": lambda d: d["playerData"]["nailUpgrades"],
        "total": 4
    },
    {
        "name": "永绽花",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e4/Everbloom.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/永绽花",
        "cur": get_collectable_amount("White Flower")
    },
]

# 任务完成信息
def get_question_complete(question_name):
    def do_get_question_complete(d):
        for tool in d["playerData"]["QuestCompletionData"]["savedData"]:
            if tool.get("Name") == question_name:
                return tool.get("Data", {}).get("IsCompleted", False)
        return False
    return do_get_question_complete

# 任务场景信息
def get_scene_bool(scene_name, item_id):
    def do_get_scene_bool(d):
        bool_list = d.get("sceneData", {}).get("persistentBools", {}).get("serializedList", [])
        for entry in bool_list:
            if entry.get("SceneName") == scene_name and entry.get("ID") == item_id:
                return entry.get("Value", False)
        return False
    return do_get_scene_bool

# 字段结构同 items ，但不计入完成度
other_items = [
    {
        "name": "骸底镇商店",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "花费300念珠在骸底镇佩珀处购买。若未购买，到第三幕时，则需从蚀阶中格林德尔处购买",
        "cur": lambda d: d["playerData"].get("PurchasedBonebottomHeartPiece", False)
    },
    {
        "name": "圣歌盟地商店",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "花费750念珠在圣歌盟地购买。完成任务商贾无踪后朱比拉娜会在圣歌盟地出售",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveShellFragment", False)
    },
    {
        "name": "暴怒兽蝇祈愿",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成祈愿暴怒兽蝇的奖励，需要击败第一只兽蝇与第四圣咏团并且进入纺络后在钟心镇接取",
        "cur": get_question_complete("Beastfly Hunt")
    },
    {
        "name": "隐秘猎手祈愿（第三幕）",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "与卡梅莉塔交谈或使用深邃挽歌进入过她的记忆后，在钟心镇接取祈愿",
        "cur": get_question_complete("Ant Trapper")
    },
    {
        "name": "竞速冠军祈愿（第三幕）",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成祈愿纺络竞速冠军，在飞毛腿斯威夫特设置的第三轮赛跑比赛中获胜",
        "cur": get_question_complete("Sprintmaster Race")
    },
    {
        "name": "暗蚀之心祈愿（第三幕）",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成主线任务寻觅：等候终局的暗蚀之心祈愿，在钟心镇接取",
        "cur": get_question_complete("Black Thread Pt5 Heart")
    },
    {
        "name": "沙噬虫道",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在沙噬虫道简单钥匙门的下方获取，在一堵易碎墙壁的后方",
        "cur": get_scene_bool("Crawl_02", "Heart Piece")
    },
    {
        "name": "深坞",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在髓骨洞窟和深坞中间的上通道",
        "cur": get_scene_bool("Dock_08", "Heart Piece")
    },
    {
        "name": "远野",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在远野织姬左上角的区域获取，需要飘泊者披风",
        "cur": get_scene_bool("Bone_East_20", "Heart Piece")
    },
    {
        "name": "甲木林",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在甲木林钟道站右边，需要完成平台跳跃挑战，中间有一堵易碎墙壁",
        "cur": get_scene_bool("Shellwood_14", "Heart Piece")
    },
    {
        "name": "圣堡机枢核心",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "圣堡机枢核心下半部分左边通道尽头",
        "cur": get_scene_bool("Song_09", "Heart Piece")
    },
    {
        "name": "低语书库",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "需要解密低语书库的移动方块",
        "cur": get_scene_bool("Library_05", "Heart Piece")
    },
    {
        "name": "雪灵山（左下角）",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "雪灵山左下角，需要雪灵披风",
        "cur": get_scene_bool("Peak_04c", "Heart Piece")
    },
    {
        "name": "远野东部",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "远野东部的骨头建筑内，需要完成战斗和岩浆逃生",
        "cur": get_scene_bool("Bone_East_LavaChallenge", "Heart Piece (1)")
    },
    {
        "name": "阿特拉织巢",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "阿特拉织巢的中部隐藏区域往右边的通道，需要织忆弦针",
        "cur": get_scene_bool("Weave_05b", "Heart Piece")
    },
    {
        "name": "蚀阶",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "蚀阶左下角的向上通道，需要蛛攀术与雪灵披风",
        "cur": get_scene_bool("Coral_19b", "Heart Piece")
    },
    {
        "name": "火灵竹丛",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "火灵竹丛右边通道尽头，需要雪灵披风",
        "cur": get_scene_bool("Wisp_07", "Heart Piece")
    },
    {
        "name": "罪石牢狱",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "罪石牢狱的右上角，需要叛教之钥与雪灵披风",
        "cur": get_scene_bool("Slab_17", "Heart Piece")
    },
    {
        "name": "腐汁泽",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "腐汁泽右边的一条通道尽头，需要飞针冲刺，通道里面挤满了沼蛆",
        "cur": get_scene_bool("Shadow_13", "Heart Piece")
    },
    {
        "name": "雪灵山（第三幕冰晶脉窟）",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在雪灵山冰晶脉窟顶端，需要灵丝升腾",
        "cur": get_scene_bool("Peak_06", "Heart Piece")
    },
    {
        "name": "钟心镇商店",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "花费270念珠从芙蕾的商店中购买，需要完成祈愿失踪送货员",
        "cur": lambda d: d["playerData"].get("PurchasedBelltownSpoolSegment", False)
    },
    {
        "name": "圣歌盟地商店",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "花费500念珠从朱比拉娜处购买，需要完成祈愿商贾无踪",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveSpoolPiece", False)
    },
    {
        "name": "小偷商店",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "花费680念珠从小偷格林德尔处购买，需要雪灵披风",
        "cur": lambda d: d["playerData"].get("purchasedGrindleSpoolPiece", False)
    },
    {
        "name": "跳蚤旅团",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "找到至少12个跳蚤并击败末代裁决者，由跳蚤旅团团长穆什卡赠予",
        "cur": lambda d: d["playerData"].get("MetCaravanTroupeLeaderJudge", False)
    },
    {
        "name": "谢尔玛祈愿",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "完成祈愿愈伤良方后，由谢尔玛赠与，需要使用白愈钥匙打开通往白愈厅的电梯",
        "cur": get_question_complete("Save Sherma")
    },
    {
        "name": "骸底镇",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于骸底镇上方被苔藓覆盖的一面可打碎的墙壁后面",
        "cur": get_scene_bool("Bone_11b", "Silk Spool")
    },
    {
        "name": "深坞右下角",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于深坞的右下角，需要蛛攀术和飞针冲刺",
        "cur": get_scene_bool("Bone_East_13", "Silk Spool")
    },
    {
        "name": "灰沼",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于灰沼，沙克拉长椅上方，需要打开气球机关，需要蛛攀术",
        "cur": get_scene_bool("Greymoor_02", "Silk Spool")
    },
    {
        "name": "罪石牢狱",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于罪石牢狱左侧的开放区域，需要被狱卒蝇抓捕至罪石牢狱，或者通过叛教之钥进入",
        "cur": get_scene_bool("Peak_01", "Silk Spool")
    },
    {
        "name": "圣堡巨扉圣门",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡巨扉圣门顶端，可以通过敲打天秤上来",
        "cur": get_scene_bool("Song_19_entrance", "Silk Spool")
    },
    {
        "name": "白愈厅",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于白愈厅的电梯井下方，需要使用白愈钥匙打开通往白愈厅的电梯",
        "cur": get_scene_bool("Ward_01", "Silk Spool")
    },
    {
        "name": "圣堡机枢核心",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于机枢核心的右下方",
        "cur": get_scene_bool("Cog_07", "Silk Spool")
    },
    {
        "name": "圣堡工厂右下方",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡工厂的右下方，从第十二席建筑师的房间向右",
        "cur": get_scene_bool("Library_11b", "Silk Spool")
    },
    {
        "name": "圣堡工厂中心",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡工厂的中心",
        "cur": get_scene_bool("Under_10", "Silk Spool")
    },
    {
        "name": "高庭顶端",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于高庭的塔楼顶端，需要蛛攀术和飞针冲刺",
        "cur": get_scene_bool("Hang_03_top", "Silk Spool")
    },
    {
        "name": "忆廊",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于忆廊的左侧，翠庭展示区域，需要从四楼进入，需要飞针冲刺和雪灵披风",
        "cur": get_scene_bool("Arborium_09", "Silk Spool")
    },
    {
        "name": "深坞左下",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于深坞，熔炉之女的左下侧",
        "cur": get_scene_bool("Dock_03c", "Silk Spool")
    },
    {
        "name": "阿特拉织巢",
        "category": "灵丝轴碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于阿特拉织巢，垂直通道的左侧，需要织忆弦针进入织巢",
        "cur": get_scene_bool("Weave_11", "Silk Spool")
    },
    {
        "name": "髓骨洞窟",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，需要蛛攀术",
        "cur": get_scene_bool("Bone_18", "Collectable Item Pickup")
    },
    {
        "name": "猎者小径",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，猎者小径区域获取",
        "cur": get_scene_bool("Ant_20", "Collectable Item Pickup")
    },
    {
        "name": "远野 / 蚀阶",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，由莫特以150念珠出售，若到第三幕中仍未购买则改为格林德尔以250念珠出售",
        "cur": lambda d: d["playerData"].get("PurchasedPilgrimsRestMemoryLocket", False) or d["playerData"].get("purchasedGrindleMemoryLocket", False)
    },
    {
        "name": "灰沼",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，灰沼区域获取",
        "cur": get_scene_bool("Greymoor_16", "Collectable Item Pickup")
    },
    {
        "name": "骸底镇",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，祈愿任务狩猎暴烈燧甲虫的回报",
        "cur": get_question_complete("Rock Rollers")
    },
    {
        "name": "钟心镇（芙蕾商店）",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": '第一幕，由芙蕾以330念珠出售；需完成主线任务“拯救：丝缚小镇”',
        "cur": lambda d: d["playerData"].get("PurchasedBelltownMemoryLocket", False)
    },
    {
        "name": "蚀阶",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，需要蛛攀术",
        "cur": get_scene_bool("Coral_02", "Collectable Item Pickup (1)")
    },
    {
        "name": "沙噬虫道",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，沙噬虫道区域获取",
        "cur": get_scene_bool("Crawl_09", "Collectable Item Pickup")
    },
    {
        "name": "腐汁泽（左下）",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，腐汁泽区域获取",
        "cur": get_scene_bool("Shadow_20", "Collectable Item Pickup (1)")
    },
    {
        "name": "圣堡钟道",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，击败幽影并从废鸣管风琴进入",
        "cur": get_scene_bool("Bellway_City", "Collectable Item Pickup")
    },
    {
        "name": "圣堡工厂",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，圣堡工厂区域获取",
        "cur": get_scene_bool("Under_08", "Collectable Item Pickup")
    },
    {
        "name": "深坞",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要简易钥匙和飞针冲刺；击败监工兄弟西格尼斯&格隆",
        "cur": get_scene_bool("Dock_13", "Collectable Item Pickup")
    },
    {
        "name": "低语书库",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，低语书库区域获取",
        "cur": get_scene_bool("Library_08", "Collectable Item Pickup")
    },
    {
        "name": "卡拉卡沙川",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要飞针冲刺",
        "cur": get_scene_bool("Coral_23", "Collectable Item Pickup")
    },
    {
        "name": "中途酒馆",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Halfway_01", "Collectable Item Pickup")
    },
    {
        "name": "忆廊",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Arborium_05", "Collectable Item Pickup")
    },
    {
        "name": "罪石牢狱",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Slab_Cell_Quiet", "Collectable Item Pickup")
    },
    {
        "name": "腐汁泽（右上）",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风，藏在一个悬挂的包裹中",
        "cur": get_scene_bool("Shadow_27", "Sack Corpse Pickup")
    },
    {
        "name": "钟心镇（第三幕）",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第三幕，需要灵丝升腾",
        "cur": get_scene_bool("Belltown", "Collectable Item Pickup")
    },
    {
        "name": "远野（第三幕）",
        "category": "忆境纪念盒（不计完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第三幕，需要灵丝升腾",
        "cur": get_scene_bool("Bone_East_25", "Collectable Item Pickup")
    },
    {
        "name": "1-髓骨洞窟",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要击败钟道兽并激活髓骨洞窟的钟殿",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_06", False)
    },
    {
        "name": "2-深坞",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "在深坞钟道兽车站左侧一堵可破坏的墙后面",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dock_16", False)
    },
    {
        "name": "3-深坞",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要疾风步，从获得疾风步的位置向左跑，然后击打房间右上角的拉杆",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_05", False)
    },
    {
        "name": "4-深坞",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要飞针冲刺，可以使用飞针抓住下方房间中央的圆环来到达上层区域",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dock_03d", False)
    },
    {
        "name": "5-猎者小径",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要击败猎者小径入口的斯卡尔禁卫，经过一段小小的平台跳跃挑战后即可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Ant_03", False)
    },
    {
        "name": "6-远野",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被关在一个笼子里，笼子前面有陷阱笼",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_17b", False)
    },
    {
        "name": "7-远野",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要流浪者披风和蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_10_Church", False)
    },
    {
        "name": "8-沙噬虫道",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被一只阿克尼叼着，打败它就能救出跳蚤",
        "cur": lambda d: d["playerData"].get("SavedFlea_Crawl_06", False)
    },
    {
        "name": "9-灰沼",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要完成腐囊虫泽的遭遇战，打开气球机关后才可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Greymoor_15b", False)
    },
    {
        "name": "10-灰沼",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "灰沼左侧塔楼的顶端，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Greymoor_06", False)
    },
    {
        "name": "11-灰沼（克拉特）",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/52/Kratt.png",
        "desc": "需要蛛攀术，该跳蚤为克拉特",
        "cur": lambda d: d["playerData"].get("CaravanLechSaved", False)
    },
    {
        "name": "12-钟心镇",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要打败碎裂者修姊，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Belltown_04", False)
    },
    {
        "name": "13-甲木林",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于一些有固定敌人的平台下方",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shellwood_03", False)
    },
    {
        "name": "14-蚀阶",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于钟道站左侧房间的顶部，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Coral_35", False)
    },
    {
        "name": "15-罪途",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "一只蟑螂在附近游荡，当靠近营救跳蚤时，它会发动攻击",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dust_12", False)
    },
    {
        "name": "16-腐汁泽",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于一堵可破坏的墙后面",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shadow_28", False)
    },
    {
        "name": "17-腐汁泽",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要穿过迷瘴",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dust_09", False)
    },
    {
        "name": "18-腐汁泽",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shadow_10", False)
    },
    {
        "name": "19-圣堡工厂",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要穿过可破坏的天花板，然后经过一些简短的平台跳跃挑战",
        "cur": lambda d: d["playerData"].get("SavedFlea_Under_23", False)
    },
    {
        "name": "20-圣堡工厂",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "房间里有很多敌人",
        "cur": lambda d: d["playerData"].get("SavedFlea_Under_21", False)
    },
    {
        "name": "21-圣咏殿",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "经过一段平台跳跃关卡后即可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Song_14", False)
    },
    {
        "name": "22-圣咏殿",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要流浪者披风或对风扇下劈",
        "cur": lambda d: d["playerData"].get("SavedFlea_Song_11", False)
    },
    {
        "name": "23-圣咏殿",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "",
        "cur": lambda d: d["playerData"].get("SavedFlea_Library_09", False)
    },
    {
        "name": "24-忆廊（巨蚤）",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/B_Huge_Flea.png",
        "desc": "需要幻羽披风，该跳蚤为巨蚤，需要打败他以驯服",
        "cur": lambda d: d["playerData"].get("tamedGiantFlea", False)
    },
    {
        "name": "25-罪石牢狱",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": '一扇被雾气笼罩的门内，可以选择"进入"',
        "cur": lambda d: d["playerData"].get("SavedFlea_Slab_Cell", False)
    },
    {
        "name": "26-罪石牢狱",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤位于休息长凳上方，在开口左上方的一个小房间里",
        "cur": lambda d: d["playerData"].get("SavedFlea_Slab_06", False)
    },
    {
        "name": "27-费耶山",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被冻在冰里，必须用针刺它才能把它弄出来",
        "cur": lambda d: d["playerData"].get("SavedFlea_Peak_05c", False)
    },
    {
        "name": "28-卡拉卡沙川",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于房间顶部，可从右侧覆盖着珊瑚的后面到达，也可以通过使用超级跳来到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Coral_24", False)
    },
    {
        "name": "29-腐殖渠（沃葛）",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/20/Vog.png",
        "desc": "该跳蚤为沃葛",
        "cur": lambda d: d["playerData"].get("MetTroupeHunterWild", False)
    },
    {
        "name": "30-低语书库",
        "category": "跳蚤",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "房间顶部可通过推动位于房间左侧中间的箱子到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Library_01", False)
    },
    {
        "name": "忆廊椅子旁",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在忆廊，位于长椅右侧的一个房间中，需要从另一侧进入",
        "cur": get_scene_bool("Arborium_04", "moss_berry_fruit")
    },
    {
        "name": "苔穴出生点左上",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在苔藓洞穴，位于初始房间左上方的房间中顶部",
        "cur": get_scene_bool("Tut_02", "moss_berry_fruit")
    },
    {
        "name": "出生点织巢左侧",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在阿特拉织巢左下部的一个隐藏房间中，位于长椅所在房间左侧",
        "cur": get_scene_bool("Weave_03", "moss_berry_fruit")
    },
    {
        "name": "苔穴出生点右上",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在苔藓洞穴右部，阿特拉织巢大门所在房间的顶部",
        "cur": get_scene_bool("Tut_01b", "moss_berry_fruit")
    },
    {
        "name": "骸底镇上空蚊子",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "前两幕中，位于骸底镇上方，被一只阿克尼叼着。第三幕中，该阿克尼移动至原位置正右方的房间内",
        "cur": lambda d: d["playerData"].get("bonetownAspidBerryCollected", False)
    },
    {
        "name": "德鲁伊下方蚊子",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在骸底镇的苔栖乡，位于苔藓德鲁伊所在房间正下方的一个隐藏房间内，被一只阿克尼叼着",
        "cur": lambda d: d["playerData"].get("mosstownAspidBerryCollected", False)
    },
    {
        "name": "漫游者教堂上空蚊子",
        "category": "苔莓（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "位于骸冢上部，被一只阿克尼叼着",
        "cur": lambda d: d["playerData"].get("bonegraveAspidBerryCollected", False)
    },
    {
        "name": "骸骨洞窟",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在猎者小径入口左侧，髓骨洞窟右上部的大型房间的左下角，引爆燧石炸开的通道尽头",
        "cur": get_scene_bool("Bone_07", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "深坞右侧宝箱",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在深坞右端与远野联通的房间左下角，一扇上锁的门后面的宝箱内",
        "cur": get_scene_bool("Dock_03", "Collectable Item Pickup")
    },
    {
        "name": "骸底镇购买",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在骸底镇由佩珀以60念珠出售。如果没有购买，则由格林德尔在风蚀长阶以120念珠出售",
        "cur": lambda d: d["playerData"].get("PurchasedBonebottomToolMetal", False)
    },
    {
        "name": "圣煲工厂",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在圣堡工厂右部一条管道的尽头，位于封印飞针冲刺的葬仪尖塔正下方的位置",
        "cur": get_scene_bool("Under_19b", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "火灵竹林上方小道旁",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在火灵竹丛顶端一块可破坏天花板的后面",
        "cur": get_scene_bool("Wisp_05", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "腐殖渠",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在腐殖渠的苍湖右端尽头",
        "cur": get_scene_bool("Aqueduct_05", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "风蚀长阶",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在风蚀长阶右上部的一个隐藏房间中，位于通往末代裁决者Boss房的长型洞穴右侧的一个洞口底部",
        "cur": get_scene_bool("Coral_32", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "圣歌盟地购买",
        "category": "制造金属",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在圣歌盟地由朱比拉娜以180念珠出售",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveToolMetal", False)
    },
]
