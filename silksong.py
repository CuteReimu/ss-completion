# 所有类别的列表，最终会按照这个列表进行排序
categories = ["红色工具", "蓝色工具", "黄色工具", "法术", "纹章", "能力", "其它", "面具碎片详情", "灵丝轴碎片详情", "跳蚤", "制造金属", "工具袋&制作匣", "忆境纪念盒（不占完成度）", "苔莓（不占完成度）", "遗物和音筒（不占完成度）"]
scene_names = ["苔藓洞穴", "骸底镇", "髓骨洞窟", "苔栖乡", "深坞", "远野", "灰沼", "钟心镇", "壳木林", "阿特拉织巢", "风蚀长阶", "巨扉圣门", "圣咏殿", "圣歌盟地", "机枢核心", "低语书库", "圣堡工厂", "高庭", "罪石牢狱", "雪灵山", "沙噬虫道", "猎者小径", "卡拉卡沙川", "忆廊", "白愈厅", "火灵竹丛", "腐殖渠", "罪途", "腐汁泽", "其它", "第三幕"]

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
        "desc": "罗盘由沙克拉以70念珠出售",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/92/Compass.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/罗盘",
        "cur": get_tool("Compass")
    },
    {
        "name": "碎壳挂坠",
        "category": "黄色工具",
        "scene": "髓骨洞窟",
        "desc": "碎壳挂坠位于髓骨洞窟左部的一个小房间中",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/f2/Shard_Pendant.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/碎壳挂坠",
        "cur": get_tool("Bone Necklace")
    },
    {
        "name": "磁石胸针",
        "category": "黄色工具",
        "scene": "骸底镇",
        "desc": "磁石胸针由骸底镇的佩珀以120念珠出售。如果进入第三幕导致骸底镇被摧毁，则由风蚀长阶的格林德尔以220念珠出售",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/22/Magnetite_Brooch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/磁石胸针",
        "cur": get_tool("Rosary Magnet")
    },
    {
        "name": "负重环带",
        "category": "黄色工具",
        "scene": "远野",
        "desc": "负重环带由朝圣者憩所的莫特以160念珠出售。如果因进入第三幕导致朝圣者憩所被破坏，则可以在莫特的尸体旁拾取",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ee/Weighted_Belt.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/负重环带",
        "cur": get_tool("Weighted Anklet")
    },
    {
        "name": "棘刺手环",
        "category": "黄色工具",
        "scene": "罪途",
        "desc": "棘刺手环位于罪途底层右侧的一个房间下部",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5e/Barbed_Bracelet.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/棘刺手环",
        "cur": get_tool("Barbed Wire")
    },
    {
        "name": "亡虫囊/壳囊",
        "category": "黄色工具",
        "scene": "沙噬虫道",
        "desc": "亡虫囊位于沙噬虫道右上部的一具尸体处。亡虫囊在钢铁之魂模式中会被壳囊替代",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fc/Dead_Bug%27s_Purse.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/亡虫囊",
        "cur": lambda d: get_tool("Dead Mans Purse")(d) or get_tool("Shell Satchel")(d)
    },
    {
        "name": "磁石骰",
        "category": "黄色工具",
        "scene": "风蚀长阶",
        "desc": "与风蚀长阶的幸运儿兰布尔进行游戏并赢光其念珠后由其赠与。击败机枢舞者或获得飞针冲刺后可在幸运儿兰布尔尸体旁拾取。进入第三幕后由格林德尔以300念珠出售",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/3a/Magnetite_Dice.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/磁石骰",
        "cur": get_tool("Magnetite Dice")
    },
    {
        "name": "迅捷脊锁",
        "category": "黄色工具",
        "scene": "圣堡工厂",
        "desc": "迅捷脊锁由圣堡工厂的第十二席建筑师以140念珠和1制造金属打造",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/05/Scuttlebrace.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/迅捷脊锁",
        "cur": get_tool("Scuttlebrace")
    },
    {
        "name": "登极握爪",
        "category": "黄色工具",
        "scene": "圣歌盟地",
        "desc": "登极握爪由圣歌盟地的朱比拉娜以350念珠出售",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fe/Ascendants_Grip.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/登极握爪",
        "cur": get_tool("Wallcling")
    },
    {
        "name": "蛛丝弦",
        "category": "黄色工具",
        "scene": "圣歌盟地",
        "desc": "完成再寻商人祈愿后，在朱比拉娜处以320念珠购买",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/bf/Spider_Strings.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛛丝弦",
        "cur": get_tool("Musician Charm")
    },
    {
        "name": "丝速脚环",
        "category": "黄色工具",
        "scene": "远野",
        "desc": "丝速脚环位于远野的辛德里尔织巢处，需施展疾风步快速踩过织巢内所有的压力板以获得",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/b3/Silkspeed_Anklets.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝速脚环",
        "cur": get_tool("Sprintmaster")
    },
    {
        "name": "窃者印记",
        "category": "黄色工具",
        "scene": "风蚀长阶",
        "desc": "窃贼印记由风蚀长阶的格林德尔以350念珠出售",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/80/Thiefs_Mark.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/窃者印记",
        "cur": get_tool("Thief Charm")
    },
    {
        "name": "直针",
        "category": "红色工具",
        "scene": "髓骨洞窟",
        "desc": "直针可以在髓骨洞窟的一座监狱中拾取，与格林德尔位于同一房间中",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/03/Straight_Pin.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/直针",
        "cur": get_tool("Straight Pin")
    },
    {
        "name": "三重镖",
        "category": "红色工具",
        "scene": "灰沼",
        "desc": "三重镖位于灰沼右部鸦虫湖上方的一个隐藏房间中，入口由一只高鸦虫看守",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a6/Tri-Pins.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/三重镖",
        "cur": get_tool("Tri Pin")
    },
    {
        "name": "蛰刺碎片",
        "category": "红色工具",
        "scene": "深坞",
        "desc": "蜇刺碎片由深坞的熔炉之女以140念珠和1制造金属打造",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/69/Sting_Shard.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛰刺碎片",
        "cur": get_tool("Sting Shard")
    },
    {
        "name": "钉刺",
        "category": "红色工具",
        "scene": "罪途",
        "desc": "钉刺由罪途的克鲁尔和班金给予，需要大黄蜂达成祈愿蟑螂内脏。如果已经进入了第三幕，则可以在克鲁尔和班金的小屋中直接拾取",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ef/Tacks.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/钉刺",
        "cur": get_tool("Tack")
    },
    {
        "name": "长针",
        "category": "红色工具",
        "scene": "壳木林",
        "desc": "长针位于壳木林，一个木蜂巢后的房间中",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/cb/Longpin.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/长针",
        "cur": get_tool("Harpoon")
    },
    {
        "name": "弧爪/曲镰",
        "category": "红色工具",
        "scene": "猎者小径",
        "desc": "弧爪由猎者小径的白斑斯卡尔以140念珠出售。如果白斑斯卡尔已经死亡，则弧爪会出现在上方的一个房间中，由一只斯卡尔守卫和一只斯卡尔长矛手看守",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/20/Curveclaw.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/弧爪",
        "cur": lambda d: get_tool("Curve Claws")(d) or get_tool("Curve Claws Upgraded")(d)
    },
    {
        "name": "投掷环",
        "category": "红色工具",
        "desc": "在达成旅者助行祈愿终迹后，沙克拉会将投掷环赠与大黄蜂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2b/Throwing_Ring.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/投掷环",
        "cur": get_tool("Shakra Ring")
    },
    {
        "name": "爆燃囊",
        "category": "红色工具",
        "scene": "灰沼",
        "desc": "爆燃囊可以在灰沼中雅纳碧的住所上方的一张制作台处使用1制造金属制作",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/b0/Pimpillo.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/爆燃囊",
        "cur": get_tool("Pimpilo")
    },
    {
        "name": "螺切刃",
        "category": "红色工具",
        "scene": "卡拉卡沙川",
        "desc": "螺切刃可以在卡拉卡沙川的珊瑚尖塔中拾取，需要大黄蜂击败狂暴的螺蝇才能到达",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0f/Conchcutter.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/螺切刃",
        "cur": get_tool("Conch Drill")
    },
    {
        "name": "丝弹（三选一）",
        "category": "红色工具",
        "desc": "损坏的工具位于腐汁泽底部的默格林织巢内。获取损坏的工具后可通过三种途径将其修复为丝弹",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/b3/Silkshot.png/72px-Silkshot.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝弹",
        "cur": lambda d: get_tool("WebShot Weaver")(d) or get_tool("WebShot Architect")(d) or get_tool("WebShot Forge")(d)
    },
    {
        "name": "掘洞钻",
        "category": "红色工具",
        "scene": "圣堡工厂",
        "desc": "掘洞钻位于圣堡工厂左下方的一张桌子上",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/59/Delvers_Drill.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/掘洞钻",
        "cur": get_tool("Screw Attack")
    },
    {
        "name": "机轮刃",
        "category": "红色工具",
        "scene": "圣堡工厂",
        "desc": "机轮刃由圣堡工厂的第十二席建筑师以360念珠和1制造金属打造",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8e/Cogwork_Wheel.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/机轮刃",
        "cur": get_tool("Cogwork Saw")
    },
    {
        "name": "齿轮蜂",
        "category": "红色工具",
        "scene": "高庭",
        "desc": "齿轮蜂可以在高庭的一张制作台处使用1制造金属制作",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/ba/Cogfly.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/齿轮蜂",
        "cur": get_tool("Cogwork Flier")
    },
    {
        "name": "念珠炮",
        "category": "红色工具",
        "scene": "高庭",
        "desc": "念珠炮可以在高庭的念珠银行中通过摧毁念珠串装机底下的装置获得，该房间被简易锁上锁",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/25/Rosary_Cannon_Loaded.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/念珠炮",
        "cur": get_tool("Rosary Cannon")
    },
    {
        "name": "电枢球",
        "category": "红色工具",
        "scene": "忆廊",
        "desc": "电枢球位于忆廊上层的一个隐藏房间，由两只忆廊使徒看守",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/75/Voltvessels.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/电枢球",
        "cur": get_tool("Lightning Rod")
    },
    {
        "name": "燧石板",
        "category": "红色工具",
        "scene": "深坞",
        "desc": "燧石板位于深坞右部的一个房间中",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/37/Flintslate.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/燧石板",
        "cur": get_tool("Flintstone")
    },
    {
        "name": "跳蚤秘酿",
        "category": "红色工具",
        "desc": "达成祈愿迷途跳蚤后跳蚤旅团会迁至灰沼，此时与格里什琴对话后，她会将跳蚤秘酿作为礼物赠予大黄蜂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d0/Flea_Brew.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/跳蚤秘酿",
        "cur": get_tool("Flea Brew")
    },
    {
        "name": "生质液瓶",
        "category": "红色工具",
        "scene": "沙噬虫道",
        "desc": "生质液瓶由沙噬虫道的炼金术士奇洛托给予，需要大黄蜂达成祈愿炼金助手",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/Plasmium_Phial.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/生质液瓶",
        "cur": get_tool("Lifeblood Syringe")
    },
    {
        "name": "德鲁伊之眼/德鲁伊双瞳",
        "category": "蓝色工具",
        "scene": "苔栖乡",
        "desc": "德鲁伊之眼由苔栖乡的苔藓德鲁伊给予，需要大黄蜂达成祈愿莓果采集。德鲁伊之眼可以升级为德鲁伊双瞳",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/13/Druid%27s_Eye.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/德鲁伊之眼",
        "cur": lambda d: get_tool("Mosscreep Tool 1")(d) or get_tool("Mosscreep Tool 2")(d)
    },
    {
        "name": "熔岩钟",
        "category": "蓝色工具",
        "scene": "深坞",
        "desc": "熔岩钟由深坞的熔炉之女以110念珠和1制造金属打造",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/72/Magma_Bell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/熔岩钟",
        "cur": get_tool("Lava Charm")
    },
    {
        "name": "护佑钟",
        "category": "蓝色工具",
        "scene": "远野",
        "desc": "护佑钟位于远野下部一个死去的炼岩工身上，在深坞的下部入口附近",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8c/Warding_Bell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/护佑钟",
        "cur": get_tool("Bell Bind")
    },
    {
        "name": "花芯囊",
        "category": "蓝色工具",
        "scene": "壳木林",
        "desc": "花芯囊由壳木林的灰根给予，需要达成祈愿花芯仪式",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/Pollip_Pouch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/花芯囊",
        "cur": get_tool("Poison Pouch")
    },
    {
        "name": "碎面甲",
        "category": "蓝色工具",
        "scene": "猎者小径",
        "desc": "裂痕面具由猎者小径的白斑斯卡尔以260念珠出售。如果白斑斯卡尔死亡，则可以在其尸体旁直接拾取裂痕面具",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/51/Fractured_Mask.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/碎面甲",
        "cur": get_tool("Fractured Mask")
    },
    {
        "name": "多重缚丝器",
        "category": "蓝色工具",
        "scene": "钟心镇",
        "desc": "多重缚丝器由钟心镇的芙蕾以880念珠出售，需要完成祈愿失踪送货员",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/19/Multibinder.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/多重缚丝器",
        "cur": get_tool("Multibind")
    },
    {
        "name": "织光仪",
        "category": "蓝色工具",
        "scene": "阿特拉织巢",
        "desc": "织光仪位于阿特拉织巢，需要打败两只苔藓之母后获得",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5f/Weavelight.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织光仪",
        "cur": get_tool("White Ring")
    },
    {
        "name": "锯齿环",
        "category": "蓝色工具",
        "scene": "圣堡工厂",
        "desc": "锯齿环可在位于圣堡工厂的第十二席建筑师处以230念珠和1制造金属购买打造",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/45/Sawtooth_Circlet.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/锯齿环",
        "cur": get_tool("Brolly Spike")
    },
    {
        "name": "注丝套针",
        "category": "蓝色工具",
        "scene": "白愈厅",
        "desc": "注丝套针可以在白愈厅右部的一张手术台上获取",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/dd/Injector_Band.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/注丝套针",
        "cur": get_tool("Quickbind")
    },
    {
        "name": "储丝延展器",
        "category": "蓝色工具",
        "scene": "圣歌盟地",
        "desc": "储丝延展器可在完成失踪商人后于圣歌盟地的朱比拉娜处以720念珠购买",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/17/Spool_Extender.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/储丝延展器",
        "cur": get_tool("Spool Extender")
    },
    {
        "name": "储备缚丝",
        "category": "蓝色工具",
        "desc": "储备缚丝可在祈愿最终会面结尾击败次席戍卫后由它赠予",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/13/Reserve_Bind.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/储备缚丝",
        "cur": get_tool("Reserve Bind")
    },
    {
        "name": "爪镜/双生爪镜",
        "category": "蓝色工具",
        "scene": "低语书库",
        "desc": "爪镜在低语书库的剧台处击败特罗比奥后由他掉落",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/f/fe/Claw_Mirror.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/爪镜",
        "cur": lambda d: get_tool("Dazzle Bind")(d) or get_tool("Dazzle Bind Upgraded")(d)
    },
    {
        "name": "记忆晶石",
        "category": "蓝色工具",
        "scene": "雪灵山",
        "desc": "记忆晶石位于雪灵山，左部长椅附近的一条冰晶通道中。这条通道遍布可破坏的冰晶，它们会在被打碎后的数秒复原",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/6b/Memory_Crystal.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/记忆晶石",
        "cur": get_tool("Revenge Crystal")
    },
    {
        "name": "撬赃钩",
        "category": "蓝色工具",
        "scene": "风蚀长阶",
        "desc": "撬赃钩可在习得飞针冲刺后于风蚀长阶的格林德尔处以740念珠购买",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/eb/Snitch_Pick.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/撬赃钩",
        "cur": get_tool("Thief Claw")
    },
    {
        "name": "伏特丝",
        "category": "蓝色工具",
        "scene": "卡拉卡沙川",
        "desc": "伏特丝由位于电荷巢穴的伏特维姆掉落",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c4/Volt_Filament.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/伏特丝",
        "cur": get_tool("Zap Imbuement")
    },
    {
        "name": "速射索",
        "category": "蓝色工具",
        "scene": "腐汁泽",
        "desc": "速射索位于腐汁泽中部的一面可破坏天花板后",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/4a/Quick_Sling.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/速射索",
        "cur": get_tool("Quick Sling")
    },
    {
        "name": "纯净花环",
        "category": "蓝色工具",
        "scene": "腐殖渠",
        "desc": "纯净花环藏在腐殖渠钟道站右下方洞窟中的一座废弃小屋处",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c2/Wreath_of_Purity.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/纯净花环",
        "cur": get_tool("Maggot Charm")
    },
    {
        "name": "长爪",
        "category": "蓝色工具",
        "scene": "腐殖渠",
        "desc": "长爪由腐殖渠的女猎手给予，需要大黄蜂达成祈愿育巢盛宴。如果进入了第三幕中，则在相同位置由幼兽给予，需要大黄蜂达成祈愿遗孤盛宴",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/73/Longclaw.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/长爪",
        "cur": get_tool("Longneedle")
    },
    {
        "name": "灵火提灯",
        "category": "蓝色工具",
        "scene": "火灵竹丛",
        "desc": "灵火提灯由位于火灵竹丛的炽焰之父掉落",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/80/Wispfire_Lantern.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵火提灯",
        "cur": get_tool("Wisp Lantern")
    },
    {
        "name": "蚤母卵",
        "category": "蓝色工具",
        "desc": "在找回全部30只迷途跳蚤后，跳蚤首领穆什卡会将蚤母卵赠与大黄蜂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a4/Egg_of_Flealia.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蚤母卵",
        "cur": get_tool("Flea Charm")
    },
    {
        "name": "针徽（第三幕）",
        "category": "蓝色工具",
        "scene": "第三幕",
        "desc": "第三幕才能获得，需要大黄蜂在祈愿针锋对决期间前往雪灵山与针姬决斗并胜利",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/50/Pin_Badge.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/针徽",
        "cur": get_tool("Pinstress Tool")
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
        "name": "织针磨砺",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/87/Needle_2_Sharpened_Needle.png/54px-Needle_2_Sharpened_Needle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织针",
        "cur": lambda d: d["playerData"]["nailUpgrades"],
        "total": 4
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
        "scene": "苔栖乡",
        "desc": "丝之矛可以在苔藓洞穴内的苔栖乡中习得",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/a/a4/Icon_SS_Silkspear.png/438px-Icon_SS_Silkspear.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝之矛",
        "cur": get_tool("Silk Spear")
    },
    {
        "name": "灵丝风暴",
        "category": "法术",
        "scene": "灰沼",
        "desc": "灵丝风暴可以在灰沼内的鸦虫湖上方习得",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8c/Icon_SS_Thread_Storm.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵丝风暴",
        "cur": get_tool("Thread Sphere")
    },
    {
        "name": "十字绣",
        "category": "法术",
        "scene": "腐汁泽",
        "desc": "十字绣可以在废鸣管风琴内击败幽影后习得",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/2/25/Icon_SS_Cross_Stitch.png/438px-Icon_SS_Cross_Stitch.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/十字绣",
        "cur": get_tool("Parry")
    },
    {
        "name": "丝刃镖",
        "category": "法术",
        "scene": "沙噬虫道",
        "desc": "丝刃冲刺可以在沙噬虫道的卡恩织巢内习得，需要演奏织忆弦针来开启织巢大门",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/87/Icon_SS_Sharpdart.png/438px-Icon_SS_Sharpdart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/丝刃镖",
        "cur": get_tool("Silk Charge")
    },
    {
        "name": "符文之怒",
        "category": "法术",
        "scene": "罪石牢狱",
        "desc": "击败原初罪者后即可习得符文之怒",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/9/91/Icon_SS_Rune_Rage.png/438px-Icon_SS_Rune_Rage.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/符文之怒",
        "cur": get_tool("Silk Bomb")
    },
    {
        "name": "苍白之爪（第三幕）",
        "category": "法术",
        "scene": "第三幕",
        "desc": "在第三幕使用灵丝升腾回到摇篮圣所后，在崇高圣母灵丝战斗场地上的断臂旁缚丝即可习得苍白之爪",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d9/Icon_SS_Pale_Nails.png/408px-Icon_SS_Pale_Nails.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/苍白之爪",
        "cur": get_tool("Silk Boss Needle")
    },
    {
        "name": "收割者纹章",
        "category": "纹章",
        "scene": "灰沼",
        "desc": "收割者纹章可以在灰沼的收割者教堂获取",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/0/0c/Reaper_Crest_Inventory.png/438px-Reaper_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/收割者纹章",
        "cur": get_tool_equips("Reaper"),
    },
    {
        "name": "漫游者纹章",
        "category": "纹章",
        "scene": "骸底镇",
        "desc": "漫游者纹章可以在苔藓洞穴左半部分的漫游者教堂获取",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/5/5e/Wanderer_Crest_Inventory.png/322px-Wanderer_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/漫游者纹章",
        "cur": get_tool_equips("Wanderer"),
    },
    {
        "name": "野兽纹章",
        "category": "纹章",
        "scene": "远野",
        "desc": "野兽纹章可以在远野的野兽教堂获取，需要先在其中击败残暴的兽蝇",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/b9/Beast_Crest_Inventory.png/438px-Beast_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/野兽纹章",
        "cur": get_tool_equips("Warrior"),
    },
    {
        "name": "建筑师纹章",
        "category": "纹章",
        "scene": "圣堡工厂",
        "desc": "建筑师纹章可以在建筑师教堂获取，需要建筑师钥匙方可进入该教堂",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d4/Architect_Crest_Inventory.png/412px-Architect_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/建筑师纹章",
        "cur": get_tool_equips("Toolmaster"),
    },
    {
        "name": "女巫纹章",
        "category": "纹章",
        "desc": "被诅咒后完成寄生手术祈愿，诅咒纹章将会转化为女巫纹章",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d0/Witch_Crest_Inventory.png/426px-Witch_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/女巫纹章",
        "cur": get_tool_equips("Witch"),
    },
    {
        "name": "萨满纹章（第三幕）",
        "category": "纹章",
        "scene": "第三幕",
        "desc": "萨满纹章可在苔藓洞穴的颓败教堂中获得，需习得灵丝升腾技艺方可抵达",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d8/Shaman_Crest_Inventory.png/435px-Shaman_Crest_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/萨满纹章",
        "cur": get_tool_equips("Spell"),
    },
    {
        "name": "疾风步",
        "category": "能力",
        "scene": "深坞",
        "desc": "在深坞最顶端习得",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/f/f2/Icon_SS_Swift_Step_Art.png/438px-Icon_SS_Swift_Step_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/疾风步",
        "cur": lambda d: d["playerData"]["hasDash"]
    },
    {
        "name": "蛛攀术",
        "category": "能力",
        "scene": "壳木林",
        "desc": "在壳木林击败碎裂者长姊打开道路后，再完成一系列平台跳跃后习得",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/3/3b/Icon_SS_Cling_Grip_Art.png/357px-Icon_SS_Cling_Grip_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛛攀术",
        "cur": lambda d: d["playerData"]["hasWalljump"]
    },
    {
        "name": "织忆弦针",
        "category": "能力",
        "scene": "钟心镇",
        "desc": "织忆弦针将在玩家击败黑寡妇并用缚丝获取其力量后习得",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c0/Icon_SS_Needolin_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/织忆弦针",
        "cur": lambda d: d["playerData"]["hasNeedolin"]
    },
    {
        "name": "飞针冲刺",
        "category": "能力",
        "scene": "圣堡工厂",
        "desc": "飞针冲刺可以穿过位于圣堡工厂的大熔釜中央房间中的一条布满熔岩的路线来习得",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/6/6f/Icon_SS_Clawline_Art.png/438px-Icon_SS_Clawline_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/飞针冲刺",
        "cur": lambda d: d["playerData"]["hasHarpoonDash"]
    },
    {
        "name": "蓄力斩",
        "category": "能力",
        "scene": "风蚀长阶",
        "desc": "大黄蜂在风蚀长阶首次与针姬相遇时，针姬会向大黄蜂提出要与其切磋练手，接受请求后便能习得蓄力斩",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/8/8e/Icon_SS_Needle_Strike_Art.png/438px-Icon_SS_Needle_Strike_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蓄力斩",
        "cur": lambda d: d["playerData"]["hasChargeSlash"]
    },
    {
        "name": "灵丝升腾（第三幕）",
        "category": "能力",
        "scene": "第三幕",
        "desc": "在深渊的阿布索伦织巢习得",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e8/Icon_SS_Silk_Soar_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵丝升腾",
        "cur": lambda d: d["playerData"]["hasSuperJump"]
    },
    {
        "name": "风铃瑶",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/0/00/Icon_SS_Sylphsong_Art.png/438px-Icon_SS_Sylphsong_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/%E9%A3%8E%E7%81%B5%E8%B0%A3",
        "cur": lambda d: d["playerData"]["HasBoundCrestUpgrader"]
    },
    {
        "name": "永绽花",
        "category": "其它",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e4/Everbloom.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/永绽花",
        "cur": get_collectable_amount("White Flower")
    },
]

# 任务完成信息
def get_quest_complete(question_name):
    def do_get_quest_complete(d):
        for tool in d["playerData"]["QuestCompletionData"]["savedData"]:
            if tool.get("Name") == question_name:
                return tool.get("Data", {}).get("IsCompleted", False)
        return False
    return do_get_quest_complete

# 任务场景信息（bool类型）
def get_scene_bool(scene_name, item_id):
    def do_get_scene_bool(d):
        bool_list = d.get("sceneData", {}).get("persistentBools", {}).get("serializedList", [])
        for entry in bool_list:
            if entry.get("SceneName") == scene_name and entry.get("ID") == item_id:
                return entry.get("Value", False)
        return False
    return do_get_scene_bool

def get_relic(relic_name):
    def do_get_relic(d):
        for tool in d["playerData"]["Relics"]["savedData"]:
            if tool.get("Name") == relic_name:
                return tool.get("Data", {}).get("IsCollected", False)
        return False
    return do_get_relic

# 字段结构同 items ，但不计入完成度
other_items = [
    {
        "name": "骸底镇商店",
        "category": "面具碎片详情",
        "scene": "骸底镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "花费300念珠在骸底镇佩珀处购买。若未购买，到第三幕时，则需从风蚀长阶中格林德尔处购买",
        "cur": lambda d: d["playerData"].get("PurchasedBonebottomHeartPiece", False)
    },
    {
        "name": "圣歌盟地商店",
        "category": "面具碎片详情",
        "scene": "圣歌盟地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "花费750念珠在圣歌盟地购买。完成任务商贾无踪后朱比拉娜会在圣歌盟地出售",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveShellFragment", False)
    },
    {
        "name": "暴怒兽蝇祈愿",
        "category": "面具碎片详情",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成祈愿暴怒兽蝇的奖励，需要击败第一只兽蝇与第四圣咏团并且进入纺络后在钟心镇接取",
        "cur": get_quest_complete("Beastfly Hunt")
    },
    {
        "name": "沙噬虫道",
        "category": "面具碎片详情",
        "scene": "沙噬虫道",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在沙噬虫道简单钥匙门的下方获取，在一堵易碎墙壁的后方",
        "cur": get_scene_bool("Crawl_02", "Heart Piece")
    },
    {
        "name": "深坞",
        "category": "面具碎片详情",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在髓骨洞窟和深坞中间的上通道",
        "cur": get_scene_bool("Dock_08", "Heart Piece")
    },
    {
        "name": "远野",
        "category": "面具碎片详情",
        "scene": "远野",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在远野织姬左上角的区域获取，需要飘泊者披风",
        "cur": get_scene_bool("Bone_East_20", "Heart Piece")
    },
    {
        "name": "壳木林",
        "category": "面具碎片详情",
        "scene": "壳木林",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在壳木林钟道站右边，需要完成平台跳跃挑战，中间有一堵易碎墙壁",
        "cur": get_scene_bool("Shellwood_14", "Heart Piece")
    },
    {
        "name": "圣堡机枢核心",
        "category": "面具碎片详情",
        "scene": "机枢核心",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "圣堡机枢核心下半部分左边通道尽头",
        "cur": get_scene_bool("Song_09", "Heart Piece")
    },
    {
        "name": "低语书库",
        "category": "面具碎片详情",
        "scene": "低语书库",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "需要解密低语书库的移动方块",
        "cur": get_scene_bool("Library_05", "Heart Piece")
    },
    {
        "name": "雪灵山（左下角）",
        "category": "面具碎片详情",
        "scene": "雪灵山",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "雪灵山左下角，需要雪灵披风",
        "cur": get_scene_bool("Peak_04c", "Heart Piece")
    },
    {
        "name": "远野东部",
        "category": "面具碎片详情",
        "scene": "远野",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "远野东部的骨头建筑内，需要完成战斗和岩浆逃生",
        "cur": get_scene_bool("Bone_East_LavaChallenge", "Heart Piece (1)")
    },
    {
        "name": "阿特拉织巢",
        "category": "面具碎片详情",
        "scene": "阿特拉织巢",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "阿特拉织巢的中部隐藏区域往右边的通道，需要织忆弦针",
        "cur": get_scene_bool("Weave_05b", "Heart Piece")
    },
    {
        "name": "风蚀长阶",
        "category": "面具碎片详情",
        "scene": "风蚀长阶",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "风蚀长阶左下角的向上通道，需要蛛攀术与雪灵披风",
        "cur": get_scene_bool("Coral_19b", "Heart Piece")
    },
    {
        "name": "火灵竹丛",
        "category": "面具碎片详情",
        "scene": "火灵竹丛",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "火灵竹丛右边通道尽头，需要雪灵披风",
        "cur": get_scene_bool("Wisp_07", "Heart Piece")
    },
    {
        "name": "罪石牢狱",
        "category": "面具碎片详情",
        "scene": "罪石牢狱",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "罪石牢狱的右上角，需要叛教之钥与雪灵披风",
        "cur": get_scene_bool("Slab_17", "Heart Piece")
    },
    {
        "name": "腐汁泽",
        "category": "面具碎片详情",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "腐汁泽右边的一条通道尽头，需要飞针冲刺，通道里面挤满了沼蛆",
        "cur": get_scene_bool("Shadow_13", "Heart Piece")
    },
    {
        "name": "雪灵山（第三幕冰晶脉窟）",
        "category": "面具碎片详情",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "在雪灵山冰晶脉窟顶端，需要灵丝升腾",
        "cur": get_scene_bool("Peak_06", "Heart Piece")
    },
    {
        "name": "隐秘猎手祈愿（第三幕）",
        "category": "面具碎片详情",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "与卡梅莉塔交谈或使用深邃挽歌进入过她的记忆后，在钟心镇接取祈愿",
        "cur": get_quest_complete("Ant Trapper")
    },
    {
        "name": "竞速冠军祈愿（第三幕）",
        "category": "面具碎片详情",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成祈愿纺络竞速冠军，在飞毛腿斯威夫特设置的第三轮赛跑比赛中获胜",
        "cur": get_quest_complete("Sprintmaster Race")
    },
    {
        "name": "暗蚀之心祈愿（第三幕）",
        "category": "面具碎片详情",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/Mask_Shard_SS.png",
        "desc": "完成主线任务寻觅：等候终局的暗蚀之心祈愿，在钟心镇接取",
        "cur": get_quest_complete("Black Thread Pt5 Heart")
    },
    {
        "name": "钟心镇商店",
        "category": "灵丝轴碎片详情",
        "scene": "钟心镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "花费270念珠从芙蕾的商店中购买，需要完成祈愿失踪送货员",
        "cur": lambda d: d["playerData"].get("PurchasedBelltownSpoolSegment", False)
    },
    {
        "name": "圣歌盟地商店",
        "category": "灵丝轴碎片详情",
        "scene": "圣歌盟地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "花费500念珠从朱比拉娜处购买，需要完成祈愿商贾无踪",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveSpoolPiece", False)
    },
    {
        "name": "格林德尔商店",
        "category": "灵丝轴碎片详情",
        "scene": "风蚀长阶",
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
        "cur": get_quest_complete("Save Sherma")
    },
    {
        "name": "骸底镇",
        "category": "灵丝轴碎片详情",
        "scene": "骸底镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于骸底镇上方被苔藓覆盖的一面可打碎的墙壁后面",
        "cur": get_scene_bool("Bone_11b", "Silk Spool")
    },
    {
        "name": "深坞右下角",
        "category": "灵丝轴碎片详情",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于深坞的右下角，需要蛛攀术和飞针冲刺",
        "cur": get_scene_bool("Bone_East_13", "Silk Spool")
    },
    {
        "name": "灰沼",
        "category": "灵丝轴碎片详情",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于灰沼，沙克拉长椅上方，需要打开气球机关，需要蛛攀术",
        "cur": get_scene_bool("Greymoor_02", "Silk Spool")
    },
    {
        "name": "罪石牢狱",
        "category": "灵丝轴碎片详情",
        "scene": "罪石牢狱",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于罪石牢狱左侧的开放区域，需要被狱卒蝇抓捕至罪石牢狱，或者通过叛教之钥进入",
        "cur": get_scene_bool("Peak_01", "Silk Spool")
    },
    {
        "name": "圣堡巨扉圣门",
        "category": "灵丝轴碎片详情",
        "scene": "巨扉圣门",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡巨扉圣门顶端，可以通过敲打天秤上来",
        "cur": get_scene_bool("Song_19_entrance", "Silk Spool")
    },
    {
        "name": "白愈厅",
        "category": "灵丝轴碎片详情",
        "scene": "白愈厅",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于白愈厅的电梯井下方，需要使用白愈钥匙打开通往白愈厅的电梯",
        "cur": get_scene_bool("Ward_01", "Silk Spool")
    },
    {
        "name": "圣堡机枢核心",
        "category": "灵丝轴碎片详情",
        "scene": "机枢核心",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于机枢核心的右下方",
        "cur": get_scene_bool("Cog_07", "Silk Spool")
    },
    {
        "name": "圣堡工厂右下方",
        "category": "灵丝轴碎片详情",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡工厂的右下方，从第十二席建筑师的房间向右",
        "cur": get_scene_bool("Library_11b", "Silk Spool")
    },
    {
        "name": "圣堡工厂中心",
        "category": "灵丝轴碎片详情",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于圣堡工厂的中心",
        "cur": get_scene_bool("Under_10", "Silk Spool")
    },
    {
        "name": "高庭顶端",
        "category": "灵丝轴碎片详情",
        "scene": "高庭",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于高庭的塔楼顶端，需要蛛攀术和飞针冲刺",
        "cur": get_scene_bool("Hang_03_top", "Silk Spool")
    },
    {
        "name": "忆廊",
        "category": "灵丝轴碎片详情",
        "scene": "忆廊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于忆廊的左侧，翠庭展示区域，需要从四楼进入，需要飞针冲刺和雪灵披风",
        "cur": get_scene_bool("Arborium_09", "Silk Spool")
    },
    {
        "name": "深坞左下",
        "category": "灵丝轴碎片详情",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于深坞，熔炉之女的左下侧",
        "cur": get_scene_bool("Dock_03c", "Silk Spool")
    },
    {
        "name": "阿特拉织巢",
        "category": "灵丝轴碎片详情",
        "scene": "阿特拉织巢",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/6/63/Spool_Fragment.png",
        "desc": "位于阿特拉织巢，垂直通道的左侧，需要织忆弦针进入织巢",
        "cur": get_scene_bool("Weave_11", "Silk Spool")
    },
    {
        "name": "髓骨洞窟",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "髓骨洞窟",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，需要蛛攀术",
        "cur": get_scene_bool("Bone_18", "Collectable Item Pickup")
    },
    {
        "name": "猎者小径",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "猎者小径",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，猎者小径区域获取",
        "cur": get_scene_bool("Ant_20", "Collectable Item Pickup")
    },
    {
        "name": "远野 / 风蚀长阶",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "远野",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，由莫特以150念珠出售，若到第三幕中仍未购买则改为格林德尔以250念珠出售",
        "cur": lambda d: d["playerData"].get("PurchasedPilgrimsRestMemoryLocket", False) or d["playerData"].get("purchasedGrindleMemoryLocket", False)
    },
    {
        "name": "灰沼",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，灰沼区域获取",
        "cur": get_scene_bool("Greymoor_16", "Collectable Item Pickup")
    },
    {
        "name": "骸底镇祈愿",
        "category": "忆境纪念盒（不占完成度）",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，祈愿任务狩猎暴烈燧甲虫的回报",
        "cur": get_quest_complete("Rock Rollers")
    },
    {
        "name": "钟心镇（芙蕾商店）",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "钟心镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": '第一幕，由芙蕾以330念珠出售；需完成主线任务“拯救：丝缚小镇”',
        "cur": lambda d: d["playerData"].get("PurchasedBelltownMemoryLocket", False)
    },
    {
        "name": "风蚀长阶",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "风蚀长阶",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，需要蛛攀术",
        "cur": get_scene_bool("Coral_02", "Collectable Item Pickup (1)")
    },
    {
        "name": "沙噬虫道",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "沙噬虫道",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，沙噬虫道区域获取",
        "cur": get_scene_bool("Crawl_09", "Collectable Item Pickup")
    },
    {
        "name": "腐汁泽（左下）",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第一幕，腐汁泽区域获取",
        "cur": get_scene_bool("Shadow_20", "Collectable Item Pickup")
    },
    {
        "name": "圣堡钟道",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "圣咏殿",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，击败幽影并从废鸣管风琴进入",
        "cur": get_scene_bool("Bellway_City", "Collectable Item Pickup")
    },
    {
        "name": "圣堡工厂",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，圣堡工厂区域获取",
        "cur": get_scene_bool("Under_08", "Collectable Item Pickup")
    },
    {
        "name": "深坞",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要简易钥匙和飞针冲刺；击败监工兄弟西格尼斯&格隆",
        "cur": get_scene_bool("Dock_13", "Collectable Item Pickup")
    },
    {
        "name": "低语书库",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "低语书库",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，低语书库区域获取",
        "cur": get_scene_bool("Library_08", "Collectable Item Pickup")
    },
    {
        "name": "卡拉卡沙川",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "卡拉卡沙川",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要飞针冲刺",
        "cur": get_scene_bool("Coral_23", "Collectable Item Pickup")
    },
    {
        "name": "中途酒馆",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Halfway_01", "Collectable Item Pickup")
    },
    {
        "name": "忆廊",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "忆廊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Arborium_05", "Collectable Item Pickup")
    },
    {
        "name": "罪石牢狱",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "罪石牢狱",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风",
        "cur": get_scene_bool("Slab_Cell_Quiet", "Collectable Item Pickup")
    },
    {
        "name": "腐汁泽（右上）",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第二幕，需要幻羽披风，藏在一个悬挂的包裹中",
        "cur": get_scene_bool("Shadow_27", "Sack Corpse Pickup")
    },
    {
        "name": "钟心镇（第三幕）",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第三幕，需要灵丝升腾",
        "cur": get_scene_bool("Belltown", "Collectable Item Pickup")
    },
    {
        "name": "远野（第三幕）",
        "category": "忆境纪念盒（不占完成度）",
        "scene": "第三幕",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ac/Memory_Locket.png",
        "desc": "第三幕，需要灵丝升腾",
        "cur": get_scene_bool("Bone_East_25", "Collectable Item Pickup")
    },
    {
        "name": "1-髓骨洞窟",
        "category": "跳蚤",
        "scene": "髓骨洞窟",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要击败钟道兽并激活髓骨洞窟的钟殿",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_06", False)
    },
    {
        "name": "2-深坞",
        "category": "跳蚤",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "在深坞钟道兽车站左侧一堵可破坏的墙后面",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dock_16", False)
    },
    {
        "name": "3-深坞",
        "category": "跳蚤",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要疾风步，从获得疾风步的位置向左跑，然后击打房间右上角的拉杆",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_05", False)
    },
    {
        "name": "4-深坞",
        "category": "跳蚤",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要飞针冲刺，可以使用飞针抓住下方房间中央的圆环来到达上层区域",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dock_03d", False)
    },
    {
        "name": "5-猎者小径",
        "category": "跳蚤",
        "scene": "猎者小径",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要击败猎者小径入口的斯卡尔禁卫，经过一段小小的平台跳跃挑战后即可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Ant_03", False)
    },
    {
        "name": "6-远野",
        "category": "跳蚤",
        "scene": "远野",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被关在一个笼子里，笼子前面有陷阱笼",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_17b", False)
    },
    {
        "name": "7-远野",
        "category": "跳蚤",
        "scene": "远野",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要流浪者披风和蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Bone_East_10_Church", False)
    },
    {
        "name": "8-沙噬虫道",
        "category": "跳蚤",
        "scene": "沙噬虫道",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被一只阿克尼叼着，打败它就能救出跳蚤",
        "cur": lambda d: d["playerData"].get("SavedFlea_Crawl_06", False)
    },
    {
        "name": "9-灰沼",
        "category": "跳蚤",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要完成腐囊虫泽的遭遇战，打开气球机关后才可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Greymoor_15b", False)
    },
    {
        "name": "10-灰沼",
        "category": "跳蚤",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "灰沼左侧塔楼的顶端，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Greymoor_06", False)
    },
    {
        "name": "11-灰沼（克拉特）",
        "category": "跳蚤",
        "scene": "灰沼",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/52/Kratt.png",
        "desc": "需要蛛攀术，该跳蚤为克拉特",
        "cur": lambda d: d["playerData"].get("CaravanLechSaved", False)
    },
    {
        "name": "12-钟心镇",
        "category": "跳蚤",
        "scene": "钟心镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要打败碎裂者修姊，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Belltown_04", False)
    },
    {
        "name": "13-壳木林",
        "category": "跳蚤",
        "scene": "壳木林",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于一些有固定敌人的平台下方",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shellwood_03", False)
    },
    {
        "name": "14-风蚀长阶",
        "category": "跳蚤",
        "scene": "风蚀长阶",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于钟道站左侧房间的顶部，需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Coral_35", False)
    },
    {
        "name": "15-罪途",
        "category": "跳蚤",
        "scene": "罪途",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "一只蟑螂在附近游荡，当靠近营救跳蚤时，它会发动攻击",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dust_12", False)
    },
    {
        "name": "16-腐汁泽",
        "category": "跳蚤",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于一堵可破坏的墙后面",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shadow_28", False)
    },
    {
        "name": "17-腐汁泽",
        "category": "跳蚤",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要穿过迷瘴",
        "cur": lambda d: d["playerData"].get("SavedFlea_Dust_09", False)
    },
    {
        "name": "18-腐汁泽",
        "category": "跳蚤",
        "scene": "腐汁泽",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要蛛攀术",
        "cur": lambda d: d["playerData"].get("SavedFlea_Shadow_10", False)
    },
    {
        "name": "19-圣堡工厂",
        "category": "跳蚤",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要穿过可破坏的天花板，然后经过一些简短的平台跳跃挑战",
        "cur": lambda d: d["playerData"].get("SavedFlea_Under_23", False)
    },
    {
        "name": "20-圣堡工厂",
        "category": "跳蚤",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "房间里有很多敌人",
        "cur": lambda d: d["playerData"].get("SavedFlea_Under_21", False)
    },
    {
        "name": "21-圣咏殿",
        "category": "跳蚤",
        "scene": "圣咏殿",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "经过一段平台跳跃关卡后即可到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Song_14", False)
    },
    {
        "name": "22-圣咏殿",
        "category": "跳蚤",
        "scene": "圣咏殿",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "需要流浪者披风或对风扇下劈",
        "cur": lambda d: d["playerData"].get("SavedFlea_Song_11", False)
    },
    {
        "name": "23-圣咏殿",
        "category": "跳蚤",
        "scene": "圣咏殿",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "",
        "cur": lambda d: d["playerData"].get("SavedFlea_Library_09", False)
    },
    {
        "name": "24-忆廊（巨蚤）",
        "category": "跳蚤",
        "scene": "忆廊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/82/B_Huge_Flea.png",
        "desc": "需要幻羽披风，该跳蚤为巨蚤，需要打败他以驯服",
        "cur": lambda d: d["playerData"].get("tamedGiantFlea", False)
    },
    {
        "name": "25-罪石牢狱",
        "category": "跳蚤",
        "scene": "罪石牢狱",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": '一扇被雾气笼罩的门内，可以选择"进入"',
        "cur": lambda d: d["playerData"].get("SavedFlea_Slab_Cell", False)
    },
    {
        "name": "26-罪石牢狱",
        "category": "跳蚤",
        "scene": "罪石牢狱",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤位于休息长凳上方，在开口左上方的一个小房间里",
        "cur": lambda d: d["playerData"].get("SavedFlea_Slab_06", False)
    },
    {
        "name": "27-雪灵山",
        "category": "跳蚤",
        "scene": "雪灵山",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "跳蚤被冻在冰里，必须用针刺它才能把它弄出来",
        "cur": lambda d: d["playerData"].get("SavedFlea_Peak_05c", False)
    },
    {
        "name": "28-卡拉卡沙川",
        "category": "跳蚤",
        "scene": "卡拉卡沙川",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "位于房间顶部，可从右侧覆盖着珊瑚的后面到达，也可以通过使用超级跳来到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Coral_24", False)
    },
    {
        "name": "29-腐殖渠（沃葛）",
        "category": "跳蚤",
        "scene": "腐殖渠",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/20/Vog.png",
        "desc": "该跳蚤为沃葛",
        "cur": lambda d: d["playerData"].get("MetTroupeHunterWild", False)
    },
    {
        "name": "30-低语书库",
        "category": "跳蚤",
        "scene": "低语书库",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/d2/Flea.png",
        "desc": "房间顶部可通过推动位于房间左侧中间的箱子到达",
        "cur": lambda d: d["playerData"].get("SavedFlea_Library_01", False)
    },
    {
        "name": "忆廊椅子旁",
        "category": "苔莓（不占完成度）",
        "scene": "忆廊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在忆廊，位于长椅右侧的一个房间中，需要从另一侧进入",
        "cur": get_scene_bool("Arborium_04", "moss_berry_fruit")
    },
    {
        "name": "苔藓洞穴出生点左上",
        "category": "苔莓（不占完成度）",
        "scene": "苔藓洞穴",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在苔藓洞穴，位于初始房间左上方的房间中顶部",
        "cur": get_scene_bool("Tut_02", "moss_berry_fruit")
    },
    {
        "name": "阿特拉织巢左侧",
        "category": "苔莓（不占完成度）",
        "scene": "阿特拉织巢",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在阿特拉织巢左下部的一个隐藏房间中，位于长椅所在房间左侧",
        "cur": get_scene_bool("Weave_03", "moss_berry_fruit")
    },
    {
        "name": "苔藓洞穴出生点右上",
        "category": "苔莓（不占完成度）",
        "scene": "苔藓洞穴",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在苔藓洞穴右部，阿特拉织巢大门所在房间的顶部",
        "cur": get_scene_bool("Tut_01b", "moss_berry_fruit")
    },
    {
        "name": "骸底镇上空蚊子",
        "category": "苔莓（不占完成度）",
        "scene": "骸底镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "前两幕中，位于骸底镇上方，被一只阿克尼叼着。第三幕中，该阿克尼移动至原位置正右方的房间内",
        "cur": lambda d: d["playerData"].get("bonetownAspidBerryCollected", False)
    },
    {
        "name": "德鲁伊下方蚊子",
        "category": "苔莓（不占完成度）",
        "scene": "苔栖乡",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "在骸底镇的苔栖乡，位于苔藓德鲁伊所在房间正下方的一个隐藏房间内，被一只阿克尼叼着",
        "cur": lambda d: d["playerData"].get("mosstownAspidBerryCollected", False)
    },
    {
        "name": "漫游者教堂上空蚊子",
        "category": "苔莓（不占完成度）",
        "scene": "骸底镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/da/Mossberry.png",
        "desc": "位于骸冢上部，被一只阿克尼叼着",
        "cur": lambda d: d["playerData"].get("bonegraveAspidBerryCollected", False)
    },
    {
        "name": "髓骨洞窟",
        "category": "制造金属",
        "scene": "髓骨洞窟",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在猎者小径入口左侧，髓骨洞窟右上部的大型房间的左下角，引爆燧石炸开的通道尽头",
        "cur": get_scene_bool("Bone_07", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "深坞右侧宝箱",
        "category": "制造金属",
        "scene": "深坞",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在深坞右端与远野联通的房间左下角，一扇上锁的门后面的宝箱内",
        "cur": get_scene_bool("Dock_03", "Collectable Item Pickup")
    },
    {
        "name": "骸底镇购买",
        "category": "制造金属",
        "scene": "骸底镇",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在骸底镇由佩珀以60念珠出售。如果没有购买，则由格林德尔在风蚀长阶以120念珠出售",
        "cur": lambda d: d["playerData"].get("PurchasedBonebottomToolMetal", False)
    },
    {
        "name": "圣堡工厂",
        "category": "制造金属",
        "scene": "圣堡工厂",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在圣堡工厂右部一条管道的尽头，位于获得飞针冲刺的位置的正下方",
        "cur": get_scene_bool("Under_19b", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "火灵竹丛上方小道旁",
        "category": "制造金属",
        "scene": "火灵竹丛",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在火灵竹丛顶端一块可破坏天花板的后面",
        "cur": get_scene_bool("Wisp_05", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "腐殖渠",
        "category": "制造金属",
        "scene": "腐殖渠",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在腐殖渠的苍湖右端尽头",
        "cur": get_scene_bool("Aqueduct_05", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "风蚀长阶",
        "category": "制造金属",
        "scene": "风蚀长阶",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在风蚀长阶右上部的一个隐藏房间中，位于通往末代裁决者Boss房的长型洞穴右侧的一个洞口底部",
        "cur": get_scene_bool("Coral_32", "Collectable Item Pickup - Tool Metal")
    },
    {
        "name": "圣歌盟地购买",
        "category": "制造金属",
        "scene": "圣歌盟地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/0e/Craftmetal.png",
        "desc": "在圣歌盟地由朱比拉娜以180念珠出售",
        "cur": lambda d: d["playerData"].get("MerchantEnclaveToolMetal", False)
    },
    {
        "name":"骨卷轴",
        "desc":"远野织女右侧",
        "scene": "远野",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/e7/Bone_Scroll.png/69px-Bone_Scroll.png",
        "cur": get_relic("Bone Record Bone_East_14")
    },
    {
        "name":"骨卷轴",
        "desc":"中途酒馆右侧水池",
        "scene": "灰沼",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/e7/Bone_Scroll.png/69px-Bone_Scroll.png",
        "cur": get_relic("Bone Record Greymoor_flooded_corridor")
    },
    {
        "name":"骨卷轴",
        "desc":"圣堡工厂拿地图房间",
        "scene": "圣堡工厂",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/e7/Bone_Scroll.png/69px-Bone_Scroll.png",
        "cur": get_relic("Bone Record Understore_Map_Room")
    },
    {
        "name":"骨卷轴",
        "desc":"火灵竹丛最顶端",
        "scene": "火灵竹丛",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/e7/Bone_Scroll.png/69px-Bone_Scroll.png",
        "cur": get_relic("Bone Record Wisp Top")
    },
    {
        "name":"织者雕像",
        "desc":"骸底镇上空",
        "scene": "骸底镇",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/c/cd/Weaver_Effigy.png/49px-Weaver_Effigy.png",
        "cur": get_relic("Weaver Totem Bonetown_upper_room")
    },
    {
        "name":"织者雕像",
        "desc":"壳木林下方，被寄生后可拿",
        "scene": "壳木林",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/c/cd/Weaver_Effigy.png/49px-Weaver_Effigy.png",
        "cur": get_relic("Weaver Totem Witch")
    },
    {
        "name":"织者雕像",
        "desc":"罪石牢狱底部",
        "scene": "罪石牢狱",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/c/cd/Weaver_Effigy.png/49px-Weaver_Effigy.png",
        "cur": get_relic("Weaver Totem Slab_Bottom")
    },
    {
        "name":"圣咏戒律",
        "desc":"骸底镇上方悬崖",
        "scene": "骸底镇",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/7/77/Choral_Commandment.png/59px-Choral_Commandment.png",
        "cur": get_relic("Seal Chit Aspid_01")
    },
    {
        "name":"圣咏戒律",
        "desc":"白愈厅左侧",
        "scene": "白愈厅",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/7/77/Choral_Commandment.png/59px-Choral_Commandment.png",
        "cur": get_relic("Seal Chit Ward Corpse")
    },
    {
        "name":"圣咏戒律",
        "desc":"圣歌盟地再寻商贾后购买",
        "scene": "圣歌盟地",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/7/77/Choral_Commandment.png/59px-Choral_Commandment.png",
        "cur": get_relic("Seal Chit City Merchant")
    },
    {
        "name":"圣咏戒律（第三幕）",
        "desc":"第三幕白愈厅上冲",
        "scene": "第三幕",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/7/77/Choral_Commandment.png/59px-Choral_Commandment.png",
        "cur": get_relic("Seal Chit Silk Siphon")
    },
    {
        "name":"符文竖琴",
        "desc":"阿特拉织巢右上",
        "scene": "阿特拉织巢",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/eb/Rune_Harp.png/48px-Rune_Harp.png",
        "cur": get_relic("Weaver Record Weave_08")
    },
    {
        "name":"符文竖琴",
        "desc":"远野织巢隐藏",
        "scene": "远野",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/eb/Rune_Harp.png/48px-Rune_Harp.png",
        "cur": get_relic("Weaver Record Sprint_Challenge")
    },
    {
        "name":"符文竖琴（第三幕）",
        "desc":"第三幕高庭，指挥家身旁",
        "scene": "第三幕",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/eb/Rune_Harp.png/48px-Rune_Harp.png",
        "cur": get_relic("Weaver Record Conductor")
    },
    {
        "name":"神秘蛋（第三幕）",
        "desc":"第三幕深渊",
        "scene": "第三幕",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/44/Arcane_Egg_Silksong.png/80px-Arcane_Egg_Silksong.png",
        "cur": get_relic("Ancient Egg Abyss Middle")
    },
    {
        "name":"圣咏音筒",
        "desc":"低语书库管理员房间",
        "scene": "低语书库",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/41/Psalm_Cylinder.png/79px-Psalm_Cylinder.png",
        "cur": get_relic("Psalm Cylinder Librarian")
    },
    {
        "name":"圣咏音筒",
        "desc":"白愈厅打完boss向下",
        "scene": "白愈厅",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/41/Psalm_Cylinder.png/79px-Psalm_Cylinder.png",
        "cur": get_relic("Psalm Cylinder Ward")
    },
    {
        "name":"圣咏音筒",
        "desc":"高庭中部澡堂",
        "scene": "高庭",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/41/Psalm_Cylinder.png/79px-Psalm_Cylinder.png",
        "cur": get_relic("Psalm Cylinder Hang")
    },
    {
        "name":"圣咏音筒",
        "desc":"风蚀长阶小偷购买",
        "scene": "风蚀长阶",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/41/Psalm_Cylinder.png/79px-Psalm_Cylinder.png",
        "cur": get_relic("Psalm Cylinder Grindle")
    },
    {
        "name":"圣咏音筒",
        "desc":"低语书库右上隐藏通道",
        "scene": "低语书库",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/41/Psalm_Cylinder.png/79px-Psalm_Cylinder.png",
        "cur": get_relic("Psalm Cylinder Library Roof")
    },
    {
        "name":"圣歌音筒",
        "desc":"低语书库底部，主线必拿",
        "scene": "低语书库",
        "category": "遗物和音筒（不占完成度）",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/d/d0/Sacred_Cylinder.png/80px-Sacred_Cylinder.png",
        "cur": get_relic("Librarian Melody Cylinder")
    },
    {
        "name":"工具袋-髓骨洞窟小游戏",
        "desc":"在髓骨洞窟游玩洛迪的飞镖小游戏，完成难度一（击中15次目标）后由洛迪给予。第三幕中在洛迪所在位置附近的桌子上拾取",
        "scene": "髓骨洞窟",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e9/Tool_Pouch.png",
        "cur": lambda d: d["playerData"].get("pinGalleriesCompleted", 0) > 0 or get_scene_bool("Bone_12", "Ladybug Craft Pickup")(d)
    },
    {
        "name":"工具袋-朝圣者憩所购买",
        "desc":"前两幕中在远野的朝圣者憩所，由莫特以220念珠出售。第三幕中由风蚀长阶的格林德尔以220念珠出售",
        "scene": "远野",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e9/Tool_Pouch.png",
        "cur": lambda d: d["playerData"].get("PurchasedBelltownToolPouch", False) or d["playerData"].get("PurchasedPilgrimsRestToolPouch", False)
    },
    {
        "name":"工具袋-跳蚤旅团",
        "desc":"作为帮助跳蚤旅团旅行的回报，由旅团团长穆什卡在蚤托邦给予",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e9/Tool_Pouch.png",
        "cur": get_scene_bool("Aqueduct_05", "Caravan Troupe Leader Fleatopia NPC")
    },
    {
        "name":"工具袋-纺络虫族图鉴",
        "desc":"达成独特祈愿研习：纺络虫族图鉴后由努努在中途酒馆给予",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e9/Tool_Pouch.png",
        "cur": get_quest_complete("Journal")
    },
    {
        "name":"制作匣-熔炉之女出售",
        "desc":"在深坞，由熔炉之女以180念珠出售",
        "scene": "深坞",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5d/Crafting_Kit.png",
        "cur": lambda d: d["playerData"].get("PurchasedForgeToolKit", False)
    },
    {
        "name":"制作匣-清剿鸦虫祈愿",
        "desc":"达成祈愿清剿鸦虫后由中途酒馆的克雷吉给予",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5d/Crafting_Kit.png",
        "cur": get_quest_complete("Crow Feathers")
    },
    {
        "name":"制作匣-建筑师出售",
        "desc":"在圣堡工厂，由第十二席建筑师以450念珠出售",
        "scene": "圣堡工厂",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5d/Crafting_Kit.png",
        "cur": lambda d: d["playerData"].get("PurchasedArchitectToolKit", False)
    },
    {
        "name":"制作匣-格林德尔出售",
        "desc":"在风蚀长阶，由格林德尔以700念珠出售",
        "scene": "风蚀长阶",
        "category": "工具袋&制作匣",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5d/Crafting_Kit.png",
        "cur": lambda d: d["playerData"].get("purchasedGrindleToolKit", False)
    },
]
