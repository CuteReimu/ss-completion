export namespace main {
	
	export class ItemResult {
	    show_text: string;
	    status: number;
	    status_text: string;
	    icon: string;
	    desc: string;
	    wiki: string;
	    scene: string;
	    is_detail?: boolean;
	
	    static createFrom(source: any = {}) {
	        return new ItemResult(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.show_text = source["show_text"];
	        this.status = source["status"];
	        this.status_text = source["status_text"];
	        this.icon = source["icon"];
	        this.desc = source["desc"];
	        this.wiki = source["wiki"];
	        this.scene = source["scene"];
	        this.is_detail = source["is_detail"];
	    }
	}
	export class CategoryResult {
	    name: string;
	    items: ItemResult[];
	
	    static createFrom(source: any = {}) {
	        return new CategoryResult(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.name = source["name"];
	        this.items = this.convertValues(source["items"], ItemResult);
	    }
	
		convertValues(a: any, classs: any, asMap: boolean = false): any {
		    if (!a) {
		        return a;
		    }
		    if (a.slice && a.map) {
		        return (a as any[]).map(elem => this.convertValues(elem, classs));
		    } else if ("object" === typeof a) {
		        if (asMap) {
		            for (const key of Object.keys(a)) {
		                a[key] = new classs(a[key]);
		            }
		            return a;
		        }
		        return new classs(a);
		    }
		    return a;
		}
	}
	export class AnalyzeResult {
	    Completion: number;
	    PlayTime: string;
	    Categories: CategoryResult[];
	    SceneNames: string[];
	
	    static createFrom(source: any = {}) {
	        return new AnalyzeResult(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.Completion = source["Completion"];
	        this.PlayTime = source["PlayTime"];
	        this.Categories = this.convertValues(source["Categories"], CategoryResult);
	        this.SceneNames = source["SceneNames"];
	    }
	
		convertValues(a: any, classs: any, asMap: boolean = false): any {
		    if (!a) {
		        return a;
		    }
		    if (a.slice && a.map) {
		        return (a as any[]).map(elem => this.convertValues(elem, classs));
		    } else if ("object" === typeof a) {
		        if (asMap) {
		            for (const key of Object.keys(a)) {
		                a[key] = new classs(a[key]);
		            }
		            return a;
		        }
		        return new classs(a);
		    }
		    return a;
		}
	}
	
	
	export class Option {
	    label: string;
	    value: string;
	
	    static createFrom(source: any = {}) {
	        return new Option(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.label = source["label"];
	        this.value = source["value"];
	    }
	}

}

