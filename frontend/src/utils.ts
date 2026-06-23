import {main} from '../wailsjs/go/models';
import CategoryResult = main.CategoryResult;
import ItemResult = main.ItemResult;

const sceneOrder = {
    '其它': 98,
    '第三幕': 99,
};

export const sortResultByScene = (res: CategoryResult[]): CategoryResult[] => {
    if (!res) return [];
    const result: CategoryResult[] = [];
    const categories = new Map<string, ItemResult[]>();
    for (const r of res) {
        for (const item of r.items) {
            const scene = item.scene || '其它';
            if (!categories.has(scene)) {
                const newItem = new CategoryResult({name: scene, items: []});
                result.push(newItem);
                categories.set(scene, newItem.items);
            }
            const category = categories.get(scene);
            category.push(item);
        }
    }
    result.sort((a, b) => (sceneOrder[a.name] ?? 0) - (sceneOrder[b.name] ?? 0));
    return result;
};