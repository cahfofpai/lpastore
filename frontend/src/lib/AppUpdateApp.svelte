<script>
    import { goto, params } from "@roxi/routify"
    import { Button, Select, Textarea, TextField } from "svelte-materialify"
    import AppAddAppButton from "./AppAddAppButton.svelte"
    import { DefaultService } from "./client"

    let app_id = $params.app_id
    let app
    let editMode = false

    if (app_id) {
        DefaultService.getAppAppsIdGet(app_id).then((response) => {
            app = response
            if (!app.mobile_compatibility) {
                app.mobile_compatibility = "-1"
            }
            editMode = true
        })
    } else {
        app = {}
        // @ts-ignore
        app.mobile_compatibility = "-1"
    }

    function updateApp() {
        console.log(app)
        DefaultService.updateAppAppsIdPut(app.id, app).then(() => {
            $goto(`/apps/${app.id}`)
        })
    }

    const mobileCompatibilityItems = [
        { name: "5 (perfect)", value: "5" },
        { name: "4", value: "4" },
        { name: "3", value: "3" },
        { name: "2", value: "2" },
        { name: "1", value: "1" },
        { name: "0 (very bad)", value: "0" },
        { name: "-1 (unset)", value: "-1" },
    ]

    const appIdRules = [
        (v) => !!v || "Required",
        (v) => {
            const pattern = /^(\w{2,}\.){2}\w{2,}$/
            return (
                pattern.test(v) ||
                "Invalid app id. It must have the format <tld>.<domain>.<app name>"
            )
        },
    ]
</script>

{#if app}
    <h3>
        {#if editMode}
            Edit {app_id}
        {:else}
            Add app
        {/if}
    </h3>

    <br />

    <div style="max-width: 200px">
        <TextField bind:value={app.id} rules={appIdRules}>id</TextField>
        <br />
        <TextField bind:value={app.appdata}>appdata-url</TextField>
        <br />
        <TextField bind:value={app.name}>name</TextField>
        <br />
        <Textarea bind:value={app.description}>description</Textarea>
        <br />
        <Select
            items={mobileCompatibilityItems}
            bind:value={app.mobile_compatibility}>mobile compatibility</Select
        >
    </div>

    <br />

    <Button on:click={() => updateApp()} class="ml-4">
        {#if editMode}
            Update
        {:else}
            Save
        {/if}
        app
    </Button>
{:else}
    <h3>404 – App to edit not found</h3>
    <br />
    But you can add it instead:
    <span class="ml-4">
        <AppAddAppButton />
    </span>
{/if}
