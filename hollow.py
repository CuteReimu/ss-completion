# 所有类别的列表，最终会按照这个列表进行排序
categories = ["Boss", "战士之梦", "守梦者", "能力", "法术", "骨钉技艺", "护符", "愚人斗兽场", "神居", "其它", "面具碎片详情", "容器碎片详情", "幼虫"]

# 所有区域的列表，按区域排序时最终会按照这个列表进行排序
scene_names = ["德特茅斯", "斯莱的商店", "遗忘十字路", "幼虫奖励", "苍绿之径", "萨鲁巴的商店", "真菌荒地", "雾之峡谷", "泪水之城", "呼啸悬崖", "水晶山峰", "安息之地", "皇家水道", "古老盆地", "王国边缘", "王后花园", "深邃巢穴", "深渊", "蜂巢", "格林剧团", "神居"]

# 查询 sceneData 的布尔值
def get_scene_bool(scene_name, item_id):
    def do_get_scene_bool(d):
        bool_list = d.get("sceneData", {}).get("persistentBoolItems", [])
        for entry in bool_list:
            if entry.get("sceneName") == scene_name and entry.get("id") == item_id:
                return entry.get("activated", False)
        return False
    return do_get_scene_bool

# name：显示名称
# category: 所属类别
# cur: 当前值，类型为一个函数 (d) => cur ，会将存档解析后的完整json格式传入d参数，可以返回一个数值，也可以返回bool值（表示已收集/未收集）
# total: 总值，不填则默认为1
# multiple: 倍率（例如完成算作2点完成度），不填则默认为1
# scene: 属于哪个地图，不填默认为“其它”地图
# icon: 图标，填写一个url，可以不填。不填就去 category_icon 里面找当前 scene 的图标
# wiki: Wiki链接，填写一个url，可以不填
# desc: 简介，鼠标放上去弹出的tooltip，可以不填
items = [
    # ===== Boss =====
    {
        "name": "假骑士",
        "category": "Boss",
        "scene": "遗忘十字路",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/9/98/B_False_Knight.png/438px-B_False_Knight.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/假骑士",
        "cur": lambda d: d["playerData"].get("killedFalseKnight", False)
    },
    {
        "name": "格鲁兹之母",
        "category": "Boss",
        "scene": "遗忘十字路",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/9f/B_Gruz_Mother.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/格鲁兹之母",
        "cur": lambda d: d["playerData"].get("killedBigFly", False)
    },
    {
        "name": "躁郁的毛里克",
        "category": "Boss",
        "scene": "遗忘十字路",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/0/02/B_Brooding_Mawlek_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/躁郁的毛里克",
        "cur": lambda d: d["playerData"].get("killedMawlek", False)
    },
    {
        "name": "收藏家",
        "category": "Boss",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/d/db/The_Collector_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/收藏家",
        "cur": lambda d: d["playerData"].get("killedJarCollector", False)
    },
    {
        "name": "螳螂领主",
        "category": "Boss",
        "scene": "真菌荒地",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/5/52/B_Mantis_Lords_2.png/344px-B_Mantis_Lords_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/螳螂领主",
        "cur": lambda d: d["playerData"].get("killedMantisLord", False)
    },
    {
        "name": "叛徒领主",
        "category": "Boss",
        "scene": "王后花园",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2c/B_Traitor_Lord.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/叛徒领主",
        "cur": lambda d: d["playerData"].get("killedTraitorLord", False)
    },
    {
        "name": "灵魂大师",
        "category": "Boss",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/72/B_Soul_Master.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵魂大师",
        "cur": lambda d: d["playerData"].get("killedMageLord", False)
    },
    {
        "name": "乌姆",
        "category": "Boss",
        "scene": "雾之峡谷",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/49/B_Uumuu.png/360px-B_Uumuu.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/乌姆",
        "cur": lambda d: d["playerData"].get("killedMegaJellyfish", False)
    },
    {
        "name": "残破容器",
        "category": "Boss",
        "scene": "古老盆地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/57/Broken_Vessel_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/残破容器",
        "cur": lambda d: d["playerData"].get("killedInfectedKnight", False)
    },
    {
        "name": "诺斯克",
        "category": "Boss",
        "scene": "深邃巢穴",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e6/Nosk_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/诺斯克",
        "cur": lambda d: d["playerData"].get("killedMimicSpider", False)
    },
    {
        "name": "守望者骑士",
        "category": "Boss",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/99/B_Watcher_Knight_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/守望者骑士",
        "cur": lambda d: d["playerData"].get("killedBlackKnight", False)
    },
    {
        "name": "粪虫防御者",
        "category": "Boss",
        "scene": "皇家水道",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/26/Dung_Defender_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/粪虫防御者",
        "cur": lambda d: d["playerData"].get("killedDungDefender", False)
    },
    {
        "name": "守护者大黄蜂",
        "category": "Boss",
        "scene": "苍绿之径",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/4f/B_Hornet_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/守护者大黄蜂",
        "cur": lambda d: d["playerData"].get("hornet1Defeated", False)
    },
    {
        "name": "岗哨大黄蜂",
        "category": "Boss",
        "scene": "王国边缘",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/4f/B_Hornet_2.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/岗哨大黄蜂",
        "cur": lambda d: d["playerData"].get("hornetOutskirtsDefeated", False)
    },
    # ===== 战士之梦 =====
    {
        "name": "戈布",
        "category": "战士之梦",
        "scene": "呼啸悬崖",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/be/Gorb_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/戈布",
        "cur": lambda d: d["playerData"].get("killedGhostAladar", False)
    },
    {
        "name": "泽若",
        "category": "战士之梦",
        "scene": "安息之地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a8/Xero_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/泽若",
        "cur": lambda d: d["playerData"].get("killedGhostXero", False)
    },
    {
        "name": "胡长老",
        "category": "战士之梦",
        "scene": "真菌荒地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/8f/Elder_Hu_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/胡长老",
        "cur": lambda d: d["playerData"].get("killedGhostHu", False)
    },
    {
        "name": "马尔穆",
        "category": "战士之梦",
        "scene": "王后花园",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/84/Marmu_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/马尔穆",
        "cur": lambda d: d["playerData"].get("killedGhostMarmu", False)
    },
    {
        "name": "无眼",
        "category": "战士之梦",
        "scene": "苍绿之径",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/37/No_Eyes_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/无眼",
        "cur": lambda d: d["playerData"].get("killedGhostNoEyes", False)
    },
    {
        "name": "马科斯",
        "category": "战士之梦",
        "scene": "王国边缘",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/10/Markoth_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/马科斯",
        "cur": lambda d: d["playerData"].get("killedGhostMarkoth", False)
    },
    {
        "name": "加利安",
        "category": "战士之梦",
        "scene": "深邃巢穴",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/8/89/Galien_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/加利安",
        "cur": lambda d: d["playerData"].get("killedGhostGalien", False)
    },
    # ===== 守梦者 =====
    {
        "name": "守望者卢瑞恩",
        "category": "守梦者",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/5/5f/Lurien_Limbs.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/守望者卢瑞恩",
        "cur": lambda d: d["playerData"].get("lurienDefeated", False)
    },
    {
        "name": "教师莫诺蒙",
        "category": "守梦者",
        "scene": "雾之峡谷",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/3/39/Monomon_Body.png/228px-Monomon_Body.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/教师莫诺蒙",
        "cur": lambda d: d["playerData"].get("monomonDefeated", False)
    },
    {
        "name": "野兽赫拉",
        "category": "守梦者",
        "scene": "深邃巢穴",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/bc/B_Herrah.png/137px-B_Herrah.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/野兽赫拉",
        "cur": lambda d: d["playerData"].get("hegemolDefeated", False)
    },
    # ===== 能力 =====
    {
        "name": "蛾翼披风",
        "category": "能力",
        "scene": "苍绿之径",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a2/Icon_HK_Mothwing_Cloak.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蛾翼披风",
        "cur": lambda d: d["playerData"].get("hasDash", False),
        "multiple": 2
    },
    {
        "name": "暗影披风",
        "category": "能力",
        "scene": "深渊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/7/75/Icon_HK_Shade_Cloak.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/暗影披风",
        "cur": lambda d: d["playerData"].get("hasShadowDash", False),
        "multiple": 2
    },
    {
        "name": "螳螂爪",
        "category": "能力",
        "scene": "真菌荒地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/bf/Icon_HK_Mantis_Claw.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/螳螂爪",
        "cur": lambda d: d["playerData"].get("hasWalljump", False),
        "multiple": 2
    },
    {
        "name": "水晶之心",
        "category": "能力",
        "scene": "水晶山峰",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/e8/Icon_HK_Crystal_Heart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/水晶之心",
        "cur": lambda d: d["playerData"].get("hasSuperDash", False),
        "multiple": 2
    },
    {
        "name": "伊思玛的眼泪",
        "category": "能力",
        "scene": "皇家水道",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/2e/Icon_HK_Ismas_Tear.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/伊思玛的眼泪",
        "cur": lambda d: d["playerData"].get("hasAcidArmour", False),
        "multiple": 2
    },
    {
        "name": "帝王之翼",
        "category": "能力",
        "scene": "古老盆地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/9b/Icon_HK_Monarch_Wings.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/帝王之翼",
        "cur": lambda d: d["playerData"].get("hasDoubleJump", False),
        "multiple": 2
    },
    {
        "name": "王之印记",
        "category": "能力",
        "scene": "王国边缘",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ec/Kings_Brand_Inventory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/王之印记",
        "cur": lambda d: d["playerData"].get("hasKingsBrand", False),
        "multiple": 2
    },
    # ===== 法术 =====
    {
        "name": "复仇之魂 | 白波",
        "category": "法术",
        "scene": "遗忘十字路",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/ab/Icon_HK_Vengeful_Spirit.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/复仇之魂",
        "cur": lambda d: d["playerData"].get("fireballLevel", 0) >= 1
    },
    {
        "name": "暗影之魂 | 黑波",
        "category": "法术",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ef/Icon_HK_Shade_Soul.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/暗影之魂",
        "cur": lambda d: d["playerData"].get("fireballLevel", 0) >= 2
    },
    {
        "name": "嚎叫幽灵 | 白吼",
        "category": "法术",
        "scene": "雾之峡谷",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/1/16/Icon_HK_Howling_Wraiths.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/嚎叫幽灵",
        "cur": lambda d: d["playerData"].get("screamLevel", 0) >= 1
    },
    {
        "name": "深渊尖啸 | 黑吼",
        "category": "法术",
        "scene": "深渊",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/bf/Icon_HK_Abyss_Shriek.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/深渊尖啸",
        "cur": lambda d: d["playerData"].get("screamLevel", 0) >= 2
    },
    {
        "name": "荒芜俯冲 | 白砸",
        "category": "法术",
        "scene": "泪水之城",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/c/c3/Icon_HK_Desolate_Dive.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/荒芜俯冲",
        "cur": lambda d: d["playerData"].get("quakeLevel", 0) >= 1
    },
    {
        "name": "黑暗降临 | 黑砸",
        "category": "法术",
        "scene": "水晶山峰",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a1/Icon_HK_Descending_Dark.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/黑暗降临",
        "cur": lambda d: d["playerData"].get("quakeLevel", 0) >= 2
    },
    # ===== 其它 =====
    {
        "name": "面具",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/2/20/Ancient_Mask.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/面具碎片",
        "cur": lambda d: d["playerData"].get("maxHealthBase", 5) - 5,
        "total": 4
    },
    {
        "name": "容器",
        "category": "其它",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/4/4c/Soul_Vessel.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/容器碎片",
        "cur": lambda d: d["playerData"].get("MPReserveMax", 0) // 33,
        "total": 3
    },
    {
        "name": "骨钉升级",
        "category": "其它",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/4/4a/Nail_5_Pure_Nail.png/75px-Nail_5_Pure_Nail.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/骨钉",
        "cur": lambda d: d["playerData"].get("nailSmithUpgrades", 0),
        "total": 4
    },
    # ===== 骨钉技艺 =====
    {
        "name": "强力劈砍",
        "category": "骨钉技艺",
        "scene": "苍绿之径",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/a/a7/Icon_HK_Great_Slash_Art.png/438px-Icon_HK_Great_Slash_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/强力劈砍",
        "cur": lambda d: d["playerData"].get("hasDashSlash", False)
    },
    {
        "name": "旋风劈砍",
        "category": "骨钉技艺",
        "scene": "呼啸悬崖",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/f/f3/Icon_HK_Cyclone_Slash_Art.png/438px-Icon_HK_Cyclone_Slash_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/旋风劈砍",
        "cur": lambda d: d["playerData"].get("hasCyclone", False)
    },
    {
        "name": "冲刺劈砍",
        "category": "骨钉技艺",
        "scene": "王国边缘",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/3/3a/Icon_HK_Dash_Slash_Art.png/438px-Icon_HK_Dash_Slash_Art.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/冲刺劈砍",
        "cur": lambda d: d["playerData"].get("hasUpwardSlash", False)
    },
    # ===== 护符 =====
    {
        "name": "采集虫群",
        "category": "护符",
        "scene": "斯莱的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/8/8a/Gathering_Swarm.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/采集虫群",
        "cur": lambda d: d["playerData"].get("gotCharm_1", False)
    },
    {
        "name": "任性的指南针",
        "category": "护符",
        "scene": "德特茅斯",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/7d/Wayward_Compass.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/任性的指南针",
        "cur": lambda d: d["playerData"].get("gotCharm_2", False)
    },
    {
        "name": "幼虫之歌",
        "category": "护符",
        "scene": "幼虫奖励",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/78/Grubsong.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/幼虫之歌",
        "cur": lambda d: d["playerData"].get("gotCharm_3", False)
    },
    {
        "name": "坚硬外壳",
        "category": "护符",
        "scene": "斯莱的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/f/f2/Stalwart_Shell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/坚硬外壳",
        "cur": lambda d: d["playerData"].get("gotCharm_4", False)
    },
    {
        "name": "巴德尔之壳",
        "category": "护符",
        "scene": "呼啸悬崖",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/2/21/Baldur_Shell.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/巴德尔之壳",
        "cur": lambda d: d["playerData"].get("gotCharm_5", False)
    },
    {
        "name": "亡者之怒",
        "category": "护符",
        "scene": "德特茅斯",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/4/4f/Fury_of_the_Fallen.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/亡者之怒",
        "cur": lambda d: d["playerData"].get("gotCharm_6", False)
    },
    {
        "name": "快速聚集",
        "category": "护符",
        "scene": "萨鲁巴的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/6/6a/Quick_Focus.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/快速聚集",
        "cur": lambda d: d["playerData"].get("gotCharm_7", False)
    },
    {
        "name": "生命血之心",
        "category": "护符",
        "scene": "萨鲁巴的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/7c/Lifeblood_Heart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/生命血之心",
        "cur": lambda d: d["playerData"].get("gotCharm_8", False)
    },
    {
        "name": "生命血核心",
        "category": "护符",
        "scene": "深渊",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/8/81/Lifeblood_Core.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/生命血核心",
        "cur": lambda d: d["playerData"].get("gotCharm_9", False)
    },
    {
        "name": "防御者纹章",
        "category": "护符",
        "scene": "皇家水道",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/5/56/Defender%27s_Crest.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/防御者纹章",
        "cur": lambda d: d["playerData"].get("gotCharm_10", False)
    },
    {
        "name": "吸虫之巢",
        "category": "护符",
        "scene": "皇家水道",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/79/Flukenest.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/吸虫之巢",
        "cur": lambda d: d["playerData"].get("gotCharm_11", False)
    },
    {
        "name": "苦痛荆棘",
        "category": "护符",
        "scene": "苍绿之径",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/8/8f/Thorns_of_Agony.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/苦痛荆棘",
        "cur": lambda d: d["playerData"].get("gotCharm_12", False)
    },
    {
        "name": "骄傲印记",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/6/69/Mark_of_Pride.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/骄傲印记",
        "cur": lambda d: d["playerData"].get("gotCharm_13", False)
    },
    {
        "name": "稳定之体",
        "category": "护符",
        "scene": "萨鲁巴的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/f/f5/Steady_Body.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/稳定之体",
        "cur": lambda d: d["playerData"].get("gotCharm_14", False)
    },
    {
        "name": "沉重之击",
        "category": "护符",
        "scene": "斯莱的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/f/f6/Heavy_Blow.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/沉重之击",
        "cur": lambda d: d["playerData"].get("gotCharm_15", False)
    },
    {
        "name": "锋利之影",
        "category": "护符",
        "scene": "深邃巢穴",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/1/13/Sharp_Shadow.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/锋利之影",
        "cur": lambda d: d["playerData"].get("gotCharm_16", False)
    },
    {
        "name": "蘑菇孢子",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/78/Spore_Shroom.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蘑菇孢子",
        "cur": lambda d: d["playerData"].get("gotCharm_17", False)
    },
    {
        "name": "修长之钉",
        "category": "护符",
        "scene": "萨鲁巴的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/d/d1/Longnail.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/修长之钉",
        "cur": lambda d: d["playerData"].get("gotCharm_18", False)
    },
    {
        "name": "萨满之石",
        "category": "护符",
        "scene": "萨鲁巴的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/5/5e/Shaman_Stone.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/萨满之石",
        "cur": lambda d: d["playerData"].get("gotCharm_19", False)
    },
    {
        "name": "灵魂捕手",
        "category": "护符",
        "scene": "遗忘十字路",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/c/ca/Soul_Catcher.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/灵魂捕手",
        "cur": lambda d: d["playerData"].get("gotCharm_20", False)
    },
    {
        "name": "噬魂者",
        "category": "护符",
        "scene": "安息之地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/6/6c/Soul_Eater.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/噬魂者",
        "cur": lambda d: d["playerData"].get("gotCharm_21", False)
    },
    {
        "name": "发光子宫",
        "category": "护符",
        "scene": "遗忘十字路",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/c/c6/Glowing_Womb.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/发光子宫",
        "cur": lambda d: d["playerData"].get("gotCharm_22", False)
    },
    {
        "name": "易碎/坚固心脏",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/1/13/Fragile_Heart.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/易碎心脏",
        "cur": lambda d: d["playerData"].get("gotCharm_23", False) or d["playerData"].get("fragileHealth_unbreakable", False)
    },
    {
        "name": "易碎/坚固贪婪",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/b/b6/Fragile_Greed.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/易碎贪婪",
        "cur": lambda d: d["playerData"].get("gotCharm_24", False) or d["playerData"].get("fragileGreed_unbreakable", False)
    },
    {
        "name": "易碎/坚固力量",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/7b/Fragile_Strength.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/易碎力量",
        "cur": lambda d: d["playerData"].get("gotCharm_25", False) or d["playerData"].get("fragileStrength_unbreakable", False)
    },
    {
        "name": "骨钉大师的荣耀",
        "category": "护符",
        "scene": "德特茅斯",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/0/0f/Nailmaster%27s_Glory.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/骨钉大师的荣耀",
        "cur": lambda d: d["playerData"].get("gotCharm_26", False)
    },
    {
        "name": "乔尼的祝福",
        "category": "护符",
        "scene": "呼啸悬崖",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/6/67/Joni%27s_Blessing.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/乔尼的祝福",
        "cur": lambda d: d["playerData"].get("gotCharm_27", False)
    },
    {
        "name": "乌恩之形",
        "category": "护符",
        "scene": "苍绿之径",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/b/b4/Shape_of_Unn.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/乌恩之形",
        "cur": lambda d: d["playerData"].get("gotCharm_28", False)
    },
    {
        "name": "蜂巢之血",
        "category": "护符",
        "scene": "蜂巢",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/e/eb/Hiveblood.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蜂巢之血",
        "cur": lambda d: d["playerData"].get("gotCharm_29", False)
    },
    {
        "name": "舞梦者",
        "category": "护符",
        "scene": "安息之地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/9/94/Dream_Wielder.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/舞梦者",
        "cur": lambda d: d["playerData"].get("gotCharm_30", False)
    },
    {
        "name": "冲刺大师",
        "category": "护符",
        "scene": "真菌荒地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/7/70/Dashmaster.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/冲刺大师",
        "cur": lambda d: d["playerData"].get("gotCharm_31", False)
    },
    {
        "name": "快速劈砍",
        "category": "护符",
        "scene": "王国边缘",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/5/5f/Quick_Slash.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/快速劈砍",
        "cur": lambda d: d["playerData"].get("gotCharm_32", False)
    },
    {
        "name": "法术扭曲者",
        "category": "护符",
        "scene": "泪水之城",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/3/33/Spell_Twister.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/法术扭曲者",
        "cur": lambda d: d["playerData"].get("gotCharm_33", False)
    },
    {
        "name": "深度聚集",
        "category": "护符",
        "scene": "水晶山峰",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/e/ea/Deep_Focus.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/深度聚集",
        "cur": lambda d: d["playerData"].get("gotCharm_34", False)
    },
    {
        "name": "蜕变挽歌",
        "category": "护符",
        "scene": "幼虫奖励",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/b/bd/Grubberfly%27s_Elegy.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蜕变挽歌",
        "cur": lambda d: d["playerData"].get("gotCharm_35", False)
    },
    {
        "name": "国王之魂/虚空之心",
        "category": "护符",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/3/34/Kingsoul.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/国王之魂",
        "cur": lambda d: (d["playerData"].get("gotQueenFragment", False) and d["playerData"].get("gotKingFragment", False)) or d["playerData"].get("gotShadeCharm", False)
    },
    {
        "name": "飞毛腿",
        "category": "护符",
        "scene": "斯莱的商店",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/e/e9/Sprintmaster.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/飞毛腿",
        "cur": lambda d: d["playerData"].get("gotCharm_37", False)
    },
    {
        "name": "梦之盾",
        "category": "护符",
        "scene": "安息之地",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/4/47/Dreamshield.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/梦之盾",
        "cur": lambda d: d["playerData"].get("gotCharm_38", False)
    },
    {
        "name": "编织者之歌",
        "category": "护符",
        "scene": "深邃巢穴",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/2/26/Weaversong.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/编织者之歌",
        "cur": lambda d: d["playerData"].get("gotCharm_39", False)
    },
    {
        "name": "格林之子/无忧旋律",
        "category": "护符",
        "scene": "格林剧团",
        "icon": "https://cdn.wikimg.net/en/hkwiki/images/9/91/Grimmchild.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/格林之子",
        "cur": lambda d: d["playerData"].get("gotCharm_40", False)
    },
    # ===== 梦之钉 =====
    {
        "name": "获得梦之钉",
        "category": "其它",
        "scene": "安息之地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/a/a2/Icon_HK_Dream_Nail.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/梦之钉",
        "cur": lambda d: d["playerData"].get("hasDreamNail", False)
    },
    {
        "name": "觉醒梦之钉",
        "category": "其它",
        "scene": "安息之地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/b0/Icon_HK_Awoken_Dream_Nail.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/梦之钉",
        "cur": lambda d: d["playerData"].get("dreamNailUpgraded", False)
    },
    {
        "name": "先知升天",
        "category": "其它",
        "scene": "安息之地",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/e/ee/Seer.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/先知",
        "cur": lambda d: d["playerData"].get("mothDeparted", False)
    },
    # ===== 愚人斗兽场 =====
    {
        "name": "勇士的试炼",
        "category": "愚人斗兽场",
        "scene": "王国边缘",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/b/b0/Trial_of_the_Warrior.png/150px-Trial_of_the_Warrior.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/勇士的试炼",
        "cur": lambda d: d["playerData"].get("colosseumBronzeCompleted", False)
    },
    {
        "name": "征服者的试炼",
        "category": "愚人斗兽场",
        "scene": "王国边缘",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/0/05/Trial_of_the_Conqueror.png/150px-Trial_of_the_Conqueror.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/征服者的试炼",
        "cur": lambda d: d["playerData"].get("colosseumSilverCompleted", False)
    },
    {
        "name": "愚人的试炼",
        "category": "愚人斗兽场",
        "scene": "王国边缘",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/c/ca/Trial_of_the_Fool.png/150px-Trial_of_the_Fool.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/愚人的试炼",
        "cur": lambda d: d["playerData"].get("colosseumGoldCompleted", False)
    },
    # ===== 格林剧团 =====
    {
        "name": "格林",
        "category": "Boss",
        "scene": "格林剧团",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/b/ba/Grimm_Idle.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/格林",
        "cur": lambda d: d["playerData"].get("killedGrimm", False)
    },
    {
        "name": "梦魇之王格林（也可放逐）",
        "category": "Boss",
        "scene": "格林剧团",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/9/95/Nightmare_King_without_Essence.png/276px-Nightmare_King_without_Essence.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/梦魇之王格林",
        "cur": lambda d: d["playerData"].get("killedNightmareGrimm", False) or d["playerData"].get("destroyedNightmareLantern", False)
    },
    # ===== 蜂巢 =====
    {
        "name": "蜂巢骑士",
        "category": "Boss",
        "scene": "蜂巢",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/3/3b/B_Hive_Knight.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/蜂巢骑士",
        "cur": lambda d: d["playerData"].get("killedHiveKnight", False)
    },
    # ===== 神居 =====
    {
        "name": "神明调谐器",
        "category": "神居",
        "scene": "神居",
        "icon": "https://huiji-public.huijistatic.com/hkss/uploads/9/92/Godtuner.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/神明调谐器",
        "cur": lambda d: d["playerData"].get("hasGodfinder", False)
    },
    {
        "name": "大师万神殿",
        "category": "神居",
        "scene": "神居",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/6/6b/Pantheon_of_the_Master.png/300px-Pantheon_of_the_Master.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/大师万神殿",
        "cur": lambda d: d["playerData"].get("bossDoorStateTier1", {}).get("completed", False)
    },
    {
        "name": "艺术家万神殿",
        "category": "神居",
        "scene": "神居",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/1/1a/Pantheon_of_the_Artist.png/300px-Pantheon_of_the_Artist.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/艺术家万神殿",
        "cur": lambda d: d["playerData"].get("bossDoorStateTier2", {}).get("completed", False)
    },
    {
        "name": "贤者万神殿",
        "category": "神居",
        "scene": "神居",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/a/ad/Pantheon_of_the_Sage.png/300px-Pantheon_of_the_Sage.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/贤者万神殿",
        "cur": lambda d: d["playerData"].get("bossDoorStateTier3", {}).get("completed", False)
    },
    {
        "name": "骑士万神殿",
        "category": "神居",
        "scene": "神居",
        "icon": "https://huiji-thumb.huijistatic.com/hkss/uploads/thumb/e/e4/Pantheon_of_the_Knight.png/300px-Pantheon_of_the_Knight.png",
        "wiki": "https://hkss.huijiwiki.com/wiki/骑士万神殿",
        "cur": lambda d: d["playerData"].get("bossDoorStateTier4", {}).get("completed", False)
    },
]

# 字段结构同 items ，但不计入完成度
other_items = [
    # ===== 面具碎片详情 =====
    {
        "name": "斯莱商店（1）",
        "category": "面具碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyShellFrag1", False)
    },
    {
        "name": "斯莱商店（2）",
        "category": "面具碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyShellFrag2", False)
    },
    {
        "name": "斯莱商店（3）",
        "category": "面具碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyShellFrag3", False)
    },
    {
        "name": "斯莱商店（4）",
        "category": "面具碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyShellFrag4", False)
    },
    {
        "name": "先知给予",
        "category": "面具碎片详情",
        "scene": "安息之地",
        "cur": lambda d: d["playerData"].get("dreamReward8", False)
    },
    {
        "name": "毛里克巢穴",
        "category": "面具碎片详情",
        "scene": "遗忘十字路",
        "desc": "遗忘十字路左部，杀死躁郁的毛里克的奖励",
        "cur": get_scene_bool("Crossroads_13", "Heart Piece")
    },
    {
        "name": "虫爷爷赠予",
        "category": "面具碎片详情",
        "scene": "幼虫奖励",
        "desc": "由虫爷爷赠予，需要营救5只幼虫",
        "cur": get_scene_bool("Crossroads_38", "Heart Piece")
    },
    {
        "name": "遗忘十字路",
        "category": "面具碎片详情",
        "scene": "遗忘十字路",
        "desc": "遗忘十字路，假骑士下方有很多戈姆处，推荐先获取螳螂爪，或使用下劈",
        "cur": get_scene_bool("Crossroads_09", "Heart Piece")
    },
    {
        "name": "布蕾塔房间",
        "category": "面具碎片详情",
        "scene": "德特茅斯",
        "desc": "德特茅斯布蕾塔的屋子里，需要在真菌荒地救出布蕾塔",
        "cur": get_scene_bool("Room_Bretta", "Heart Piece")
    },
    {
        "name": "王后驿站",
        "category": "面具碎片详情",
        "scene": "真菌荒地",
        "desc": "王后驿站右部，需要螳螂爪",
        "cur": get_scene_bool("Fungus2_01", "Heart Piece")
    },
    {
        "name": "石之庇护所",
        "category": "面具碎片详情",
        "scene": "苍绿之径",
        "desc": "苍绿之径的石之庇护所，推荐先获取光蝇灯笼",
        "cur": get_scene_bool("Fungus1_36", "Heart Piece")
    },
    {
        "name": "皇家水道",
        "category": "面具碎片详情",
        "scene": "皇家水道",
        "desc": "皇家水道左上部，游到左边的房间主道下",
        "cur": get_scene_bool("Waterways_04b", "Heart Piece")
    },
    {
        "name": "水晶山峰",
        "category": "面具碎片详情",
        "scene": "水晶山峰",
        "desc": "水晶山峰，击败暴怒守卫的奖励，需要帝王之翼",
        "cur": get_scene_bool("Mines_32", "Heart Piece")
    },
    {
        "name": "深邃巢穴",
        "category": "面具碎片详情",
        "scene": "深邃巢穴",
        "desc": "通过真菌核心进入深邃巢穴，在螳螂领主附近，需要帝王之翼",
        "cur": get_scene_bool("Fungus2_25", "Heart Piece")
    },
    {
        "name": "蜂巢",
        "category": "面具碎片详情",
        "scene": "蜂巢",
        "desc": "在蜂巢的一堵墙后，需要引蜂巢守卫撞碎墙壁",
        "cur": get_scene_bool("Hive_04", "Heart Piece")
    },
    {
        "name": "送花任务",
        "category": "面具碎片详情",
        "desc": "由安息之地的灰色哀悼者给予，需要完成送娇嫩的花的任务",
        "cur": get_scene_bool("Room_Mansion", "Heart Piece")
    },
    # ===== 容器碎片详情 =====
    {
        "name": "斯莱商店（1）",
        "category": "容器碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyVesselFrag1", False)
    },
    {
        "name": "斯莱商店（2）",
        "category": "容器碎片详情",
        "scene": "斯莱的商店",
        "cur": lambda d: d["playerData"].get("slyVesselFrag2", False)
    },
    {
        "name": "先知给予",
        "category": "容器碎片详情",
        "scene": "安息之地",
        "cur": lambda d: d["playerData"].get("dreamReward5", False)
    },
    {
        "name": "鹿角虫巢穴",
        "category": "容器碎片详情",
        "scene": "呼啸悬崖",
        "cur": lambda d: d["playerData"].get("vesselFragStagNest", False)
    },
    {
        "name": "苍绿之径",
        "category": "容器碎片详情",
        "scene": "苍绿之径",
        "desc": "苍绿之径中，通往王后花园但无法从这侧打开的入口附近",
        "cur": get_scene_bool("Fungus1_13", "Vessel Fragment")
    },
    {
        "name": "遗忘十字路",
        "category": "容器碎片详情",
        "scene": "遗忘十字路",
        "desc": "遗忘十字路电梯左边，需要在泪水之城解锁电梯",
        "cur": get_scene_bool("Crossroads_37", "Vessel Fragment")
    },
    {
        "name": "国王驿站",
        "category": "容器碎片详情",
        "scene": "泪水之城",
        "desc": "国王驿站上方的电梯旁，通过遭遇战后",
        "cur": get_scene_bool("Ruins2_09", "Vessel Fragment")
    },
    {
        "name": "深邃巢穴",
        "category": "容器碎片详情",
        "scene": "深邃巢穴",
        "desc": "深邃巢穴可使用的电车上方",
        "cur": get_scene_bool("Deepnest_38", "Vessel Fragment")
    },
    {
        "name": "古老盆地",
        "category": "容器碎片详情",
        "scene": "古老盆地",
        "desc": "向古老盆地喷泉中投入3000吉欧获得",
        "cur": get_scene_bool("Abyss_04", "Vessel Fragment")
    },
    # ===== 幼虫 =====
    {
        "name": "1-遗忘十字路",
        "category": "幼虫",
        "scene": "遗忘十字路",
        "desc": "黑卵圣殿右侧，需要打败/绕过躯壳守卫",
        "cur": get_scene_bool("Crossroads_48", "Grub Bottle")
    },
    {
        "name": "2-遗忘十字路",
        "category": "幼虫",
        "scene": "遗忘十字路",
        "desc": "靠近雾之峡谷的入口",
        "cur": get_scene_bool("Crossroads_35", "Grub Bottle")
    },
    {
        "name": "3-遗忘十字路",
        "category": "幼虫",
        "scene": "遗忘十字路",
        "desc": "需要打破可破坏的墙壁",
        "cur": get_scene_bool("Crossroads_03", "Grub Bottle")
    },
    {
        "name": "4-遗忘十字路",
        "category": "幼虫",
        "scene": "遗忘十字路",
        "desc": "需要下批跳过刺",
        "cur": get_scene_bool("Crossroads_31", "Grub Bottle")
    },
    {
        "name": "5-遗忘十字路",
        "category": "幼虫",
        "scene": "遗忘十字路",
        "desc": "需要蛾翼披风或对刺下劈",
        "cur": get_scene_bool("Crossroads_05", "Grub Bottle")
    },
    {
        "name": "6-苍绿之径",
        "category": "幼虫",
        "scene": "苍绿之径",
        "desc": "",
        "cur": get_scene_bool("Fungus1_06", "Grub Bottle")
    },
    {
        "name": "7-苍绿之径",
        "category": "幼虫",
        "scene": "苍绿之径",
        "desc": "",
        "cur": get_scene_bool("Fungus1_07", "Grub Bottle")
    },
    {
        "name": "8-苍绿之径",
        "category": "幼虫",
        "scene": "苍绿之径",
        "desc": "需要打败苔藓骑士",
        "cur": get_scene_bool("Fungus1_21", "Grub Bottle")
    },
    {
        "name": "9-苍绿之径",
        "category": "幼虫",
        "scene": "苍绿之径",
        "desc": "需要蛾翼披风",
        "cur": get_scene_bool("Fungus1_13", "Grub Bottle")
    },
    {
        "name": "10-真菌荒地",
        "category": "幼虫",
        "scene": "真菌荒地",
        "desc": "需要蛾翼披风",
        "cur": get_scene_bool("Fungus2_18", "Grub Bottle")
    },
    {
        "name": "11-真菌荒地",
        "category": "幼虫",
        "scene": "真菌荒地",
        "desc": "需要螳螂爪",
        "cur": get_scene_bool("Fungus2_20", "Grub Bottle")
    },
    {
        "name": "12-泪水之城",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "",
        "cur": get_scene_bool("Ruins1_05", "Grub Bottle")
    },
    {
        "name": "13-泪水之城",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "",
        "cur": get_scene_bool("Ruins_House_01", "Grub Bottle")
    },
    {
        "name": "14-泪水之城",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "",
        "cur": get_scene_bool("Ruins1_32", "Grub Bottle")
    },
    {
        "name": "15-泪水之城",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "",
        "cur": get_scene_bool("Ruins2_07", "Grub Bottle")
    },
    {
        "name": "16-泪水之城",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "",
        "cur": get_scene_bool("Ruins2_03", "Grub Bottle")
    },
    {
        "name": "17-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要蛾翼披风和螳螂爪",
        "cur": get_scene_bool("Mines_16", "Grub Bottle")
    },
    {
        "name": "18-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要水晶之心",
        "cur": get_scene_bool("Mines_19", "Grub Bottle")
    },
    {
        "name": "19-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要帝王之翼",
        "cur": get_scene_bool("Mines_31", "Grub Bottle")
    },
    {
        "name": "20-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要水晶之心",
        "cur": get_scene_bool("Mines_24", "Grub Bottle")
    },
    {
        "name": "21-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要蛾翼披风",
        "cur": get_scene_bool("Mines_03", "Grub Bottle")
    },
    {
        "name": "22-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "",
        "cur": get_scene_bool("Mines_04", "Grub Bottle")
    },
    {
        "name": "23-水晶山峰",
        "category": "幼虫",
        "scene": "水晶山峰",
        "desc": "需要进行平台跳跃/跳跳乐",
        "cur": get_scene_bool("Mines_35", "Grub Bottle")
    },
    {
        "name": "24-安息之地",
        "category": "幼虫",
        "scene": "安息之地",
        "desc": "需要荒芜俯冲",
        "cur": get_scene_bool("RestingGrounds_10", "Grub Bottle")
    },
    {
        "name": "25-皇家水道",
        "category": "幼虫",
        "scene": "皇家水道",
        "desc": "",
        "cur": get_scene_bool("Waterways_04", "Grub Bottle")
    },
    {
        "name": "26-皇家水道",
        "category": "幼虫",
        "scene": "皇家水道",
        "desc": "需要水晶之心或伊思玛的眼泪",
        "cur": get_scene_bool("Waterways_14", "Grub Bottle")
    },
    {
        "name": "27-伊思玛森林",
        "category": "幼虫",
        "scene": "皇家水道",
        "desc": "需要伊思玛的眼泪",
        "cur": get_scene_bool("Waterways_13", "Grub Bottle")
    },
    {
        "name": "28-呼啸悬崖",
        "category": "幼虫",
        "scene": "呼啸悬崖",
        "desc": "需要螳螂爪",
        "cur": get_scene_bool("Fungus1_28", "Grub Bottle")
    },
    {
        "name": "29-王国边缘",
        "category": "幼虫",
        "scene": "王国边缘",
        "desc": "需要荒芜俯冲",
        "cur": get_scene_bool("Deepnest_East_14", "Grub Bottle")
    },
    {
        "name": "30-王国边缘",
        "category": "幼虫",
        "scene": "王国边缘",
        "desc": "需要螳螂爪",
        "cur": get_scene_bool("Deepnest_East_11", "Grub Bottle")
    },
    {
        "name": "31-雾之峡谷",
        "category": "幼虫",
        "scene": "雾之峡谷",
        "desc": "需要水晶之心",
        "cur": get_scene_bool("Fungus3_47", "Grub Bottle")
    },
    {
        "name": "32-王后花园",
        "category": "幼虫",
        "scene": "王后花园",
        "desc": "",
        "cur": get_scene_bool("Fungus3_10", "Grub Bottle")
    },
    {
        "name": "33-王后花园",
        "category": "幼虫",
        "scene": "王后花园",
        "desc": "需要所有能力",
        "cur": get_scene_bool("Fungus3_22", "Grub Bottle")
    },
    {
        "name": "34-王后花园",
        "category": "幼虫",
        "scene": "王后花园",
        "desc": "需要螳螂爪",
        "cur": get_scene_bool("Fungus3_48", "Grub Bottle")
    },
    {
        "name": "35-深邃巢穴",
        "category": "幼虫",
        "scene": "深邃巢穴",
        "desc": "需要打破隐藏的可以破坏的墙壁",
        "cur": get_scene_bool("Deepnest_36", "Grub Bottle")
    },
    {
        "name": "36-深邃巢穴",
        "category": "幼虫",
        "scene": "深邃巢穴",
        "desc": "需要打破隐藏的可以破坏的墙壁",
        "cur": get_scene_bool("Deepnest_03", "Grub Bottle")
    },
    {
        "name": "37-深邃巢穴",
        "category": "幼虫",
        "scene": "深邃巢穴",
        "desc": "需要水晶之心",
        "cur": get_scene_bool("Deepnest_31", "Grub Bottle")
    },
    {
        "name": "38-深邃巢穴",
        "category": "幼虫",
        "scene": "深邃巢穴",
        "desc": "",
        "cur": get_scene_bool("Deepnest_39", "Grub Bottle")
    },
    {
        "name": "39-深邃巢穴",
        "category": "幼虫",
        "scene": "深邃巢穴",
        "desc": "",
        "cur": get_scene_bool("Deepnest_Spider_Town", "Grub Bottle")
    },
    {
        "name": "40-古老盆地",
        "category": "幼虫",
        "scene": "古老盆地",
        "desc": "需要蛾翼披风和帝王之翼",
        "cur": get_scene_bool("Abyss_19", "Grub Bottle")
    },
    {
        "name": "41-古老盆地",
        "category": "幼虫",
        "scene": "古老盆地",
        "desc": "需要荒芜俯冲",
        "cur": get_scene_bool("Abyss_17", "Grub Bottle")
    },
    {
        "name": "42-蜂巢",
        "category": "幼虫",
        "scene": "蜂巢",
        "desc": "需要荒芜俯冲和伊思玛的眼泪",
        "cur": get_scene_bool("Hive_03", "Grub Bottle")
    },
    {
        "name": "43-蜂巢",
        "category": "幼虫",
        "scene": "蜂巢",
        "desc": "需要荒芜俯冲，伊思玛的眼泪和帝王之翼",
        "cur": get_scene_bool("Hive_04", "Grub Bottle")
    },
    {
        "name": "44-46-爱之塔",
        "category": "幼虫",
        "scene": "泪水之城",
        "desc": "需要爱之钥并打败收藏家，可以一次性解救3只幼虫。需要注意，若解救任何1只后直接退出游戏的话会导致剩下幼虫消失的bug",
        "cur": get_scene_bool("Ruins2_11", "Grub Bottle")
    },
]

category_icon = {
    "面具碎片详情": "https://huiji-public.huijistatic.com/hkss/uploads/6/69/Mask_Shard.png",
    "容器碎片详情": "https://huiji-public.huijistatic.com/hkss/uploads/2/29/Vessel_Fragment.png",
    "幼虫": "https://huiji-public.huijistatic.com/hkss/uploads/0/0c/Grub.png",
}