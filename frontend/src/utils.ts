import {main} from '../wailsjs/go/models';
import AnalyzeResult = main.AnalyzeResult;
import CategoryResult = main.CategoryResult;
import ItemResult = main.ItemResult;

export const sortResultByScene = (res?: AnalyzeResult): CategoryResult[] => {
    if (!res || !res.Categories) return [];
    const result: CategoryResult[] = [];
    const categories = new Map<string, ItemResult[]>();
    for (const c of res.Categories) {
        for (const item of c.items) {
            const scene = item.scene || '其它';
            if (!categories.has(scene)) {
                const newItem = new CategoryResult({name: scene, items: []});
                result.push(newItem);
                categories.set(scene, newItem.items);
            }
            const category = categories.get(scene)!;
            if (item.is_detail && item.scene !== "第三幕" && item.scene !=="其它" && !c.name.includes("遗物和音筒") && !c.name.includes("工具") && !c.name.includes("制作匣")) {
                category.push({...item, show_text: c.name.replace("详情", "").replace("（不占完成度）", "")});
            } else {
                category.push(item);
            }
        }
    }
    const sceneOrder = Object.fromEntries(
        res.SceneNames?.map((item, index) => [item, index]) ?? []
    );
    result.sort((a, b) => (sceneOrder[a.name] ?? 99) - (sceneOrder[b.name] ?? 99));
    return result;
};