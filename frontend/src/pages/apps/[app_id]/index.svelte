<script>
    import { goto } from "@roxi/routify"
    import { Button, Icon } from "svelte-materialify"
    import { mdiPencil } from "@mdi/js"
    import { DefaultService } from "../../../lib/client"
    import AppAddAppButton from "../../../lib/AppAddAppButton.svelte"
    export let app_id

    let app

    DefaultService.getAppAppsIdGet(app_id).then((response) => {
        app = response
    })
</script>

{#if app}
    <div class="d-flex justify-space-between">
        <div>
            <h3>{app.name}</h3>
            {app.id}
        </div>

        <Button style="float: right" on:click={() => $goto("./edit")}>
            <Icon path={mdiPencil} />
            Edit app
        </Button>
    </div>
    <br />
    {app.description}

    <br />
    <br />

    Mobile compatibility: {app.mobile_compatibility} / 5
    <br />
    AppData link: <a href={app.appdata} target="_blank">{app.appdata}</a>
{:else}
    <h3>404 – App not found</h3>
    <br />
    But you can add it now:
    <span class="ml-4">
        <AppAddAppButton />
    </span>
{/if}
