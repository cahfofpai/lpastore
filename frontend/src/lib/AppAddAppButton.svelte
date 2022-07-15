<script>
    import { goto } from "@roxi/routify"
    import { Button, Icon } from "svelte-materialify"
    import { mdiPlus } from "@mdi/js"
</script>

<Button on:click={() => $goto("/apps/add")}>
    <Icon path={mdiPlus} />
    Add app
</Button>
