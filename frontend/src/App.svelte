<script>
    import {
        mdiAllInclusive,
        mdiDotsVertical,
        mdiMagnify,
        mdiPlus,
        mdiPencil,
    } from "@mdi/js"
    import {
        MaterialApp,
        Button,
        AppBar,
        Icon,
        Menu,
        ListItem,
    } from "svelte-materialify"

    let count = 0
    const increment = () => {
        count += 1
    }

    // let app_bar_background_color = "orange darken-2"
    let app_bar_background_color = "deep-orange lighten-1"
    let app_bar_text_color = "white-text"
</script>

<MaterialApp>
    <AppBar class="{app_bar_background_color} {app_bar_text_color}">
        <span slot="title">
            <Icon path={mdiAllInclusive} class={app_bar_text_color} />
            LPAStore
        </span>
        <div style="flex-grow: 1" />
        <Button fab depressed class={app_bar_background_color}>
            <Icon path={mdiMagnify} />
        </Button>
        <Menu right>
            <div slot="activator">
                <Button fab depressed class={app_bar_background_color}>
                    <Icon path={mdiDotsVertical} />
                </Button>
            </div>
            <ListItem>
                <span slot="prepend">
                    <Icon path={mdiPlus} />
                </span>
                Add app</ListItem
            >
            <ListItem>
                <span slot="prepend">
                    <Icon path={mdiPencil} />
                </span>
                Edit app
            </ListItem>
        </Menu>
    </AppBar>
    <Menu />
    <main>
        <h3>Welcome to the LPAStore!</h3>
        <br />
        <h4>It features <b>{count}</b> apps for GNU/Linux on phones</h4>
        <br />
        <Button on:click={increment}>Add app</Button>
    </main>
</MaterialApp>

<style>
    main {
        text-align: center;
        padding: 1em;
        margin: 0 auto;
    }
</style>
