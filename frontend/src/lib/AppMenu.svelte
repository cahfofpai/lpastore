<script>
    import { AppBar, Button, Icon, Menu, ListItem } from "svelte-materialify"
    import {
        mdiAllInclusive,
        mdiDotsVertical,
        mdiMagnify,
        mdiPlus,
    } from "@mdi/js"
    import { config } from "../../app_config"
    import { url, goto } from "@roxi/routify"
</script>

<AppBar class="{config.menu.backgroundColor} {config.menu.textColor}">
    <a
        href={$url("/")}
        class="{config.menu.textColor} text-decoration-none"
        slot="title"
    >
        <Icon path={mdiAllInclusive} class={config.menu.textColor} />
        <span>{config.name}</span>
    </a>
    <div style="flex-grow: 1" />
    <Button fab depressed class={config.menu.backgroundColor}>
        <Icon path={mdiMagnify} />
    </Button>
    <Menu right>
        <div slot="activator">
            <Button fab depressed class={config.menu.backgroundColor}>
                <Icon path={mdiDotsVertical} />
            </Button>
        </div>

        <ListItem on:click={() => $goto("/apps/add")}>
            <span slot="prepend">
                <Icon path={mdiPlus} />
            </span>
            Add app
        </ListItem>
    </Menu>
</AppBar>
