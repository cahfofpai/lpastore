<script>
    import AppMenu from "../lib/AppMenu.svelte"
    import AppFooter from "../lib/AppFooter.svelte"

    import { MaterialApp } from "svelte-materialify"
</script>

<MaterialApp>
    <AppMenu />
    <main>
        <slot />
    </main>
    <AppFooter />
</MaterialApp>

<style>
    main {
        margin: 0 auto 0 auto;
        max-width: 900px;
        padding: 2em;
    }
</style>
