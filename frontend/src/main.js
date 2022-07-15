import App from "./App.svelte"
import "./assets/smui.css"
import { OpenAPI } from "./lib/client"
import { config } from "../app_config"

const app = new App({
    target: document.getElementById("app"),
})

OpenAPI.BASE = config.backend.url

export default app
