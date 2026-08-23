import {ensureCSS} from "fwtoolkit"
export class TUMApp {
    constructor(app) {
        this.app = app
    }

    init() {
        return ensureCSS([staticUrl("css/tum.css")])
    }
}
