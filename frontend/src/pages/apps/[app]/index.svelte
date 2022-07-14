<script>
    import { goto } from "@roxi/routify"
    import { Button, Icon } from "svelte-materialify"
    import { mdiPencil } from "@mdi/js"
    export let app
</script>

<div class="d-flex justify-space-between">
    <h3>{app}</h3>

    <Button style="float: right" on:click={() => $goto("./edit")}>
        <Icon path={mdiPencil} />
        Edit app
    </Button>
</div>
<br />

Showing entry for {app}
