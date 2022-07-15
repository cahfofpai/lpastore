<script>
    import { config } from "../../app_config"

    import { Button } from "svelte-materialify"
    import { goto } from "@roxi/routify"
    import AppAddAppButton from "../lib/AppAddAppButton.svelte"
    import { DefaultService } from "../lib/client"

    let app_count = 0

    DefaultService.getRootGet().then((response) => {
        app_count = response.app_count
    })
</script>

<main>
    <h3>Welcome to {config.name}!</h3>

    <br />

    <h4>It features <b>{app_count}</b> apps for GNU/Linux on phones</h4>

    <br />

    <AppAddAppButton />

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
