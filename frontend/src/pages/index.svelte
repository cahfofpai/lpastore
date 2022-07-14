<script>
    import { config } from "../../app_config"

    import { Button } from "svelte-materialify"
    import { goto } from "@roxi/routify"

    // TODO: Show actual count
    let count = "0"
</script>

<main>
    <h3>Welcome to {config.name}!</h3>

    <br />

    <h4>It features <b>{count}</b> apps for GNU/Linux on phones</h4>

    <br />

    <Button on:click={() => $goto("/apps/add")}>Add app</Button>

    <br />
    <br />

    <Button on:click={() => $goto("/apps")}>Browse all apps</Button>
</main>

<style>
    main {
        text-align: center;
        margin: 0 auto;
    }
</style>
