import { svelte } from "@sveltejs/vite-plugin-svelte"
import { defineConfig } from "vite"
import pluginRewriteAll from "vite-plugin-rewrite-all"
const { preprocess } = require("./svelte.config")

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte({ preprocess }), pluginRewriteAll()],
})
