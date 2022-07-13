<script>
    import List from "@smui/list"
    import { Item, Text, Graphic } from "@smui/list"
    import TopAppBar, { Row, Section, Title } from "@smui/top-app-bar"
    import IconButton from "@smui/icon-button"
    import MenuSurface from "@smui/menu-surface"

    let menu
</script>

<TopAppBar variant="static">
    <Row>
        <Section class="white">
            <Title class="material-icons">all_inclusive</Title>
            <Title style="padding-left: 10px;">LPAStore</Title>
        </Section>
        <Section align="end">
            <IconButton class="material-icons white">search</IconButton>
            <IconButton
                style="float: right;"
                class="material-icons white"
                on:click={menu.setOpen(true)}>more_vert</IconButton
            >
            <MenuSurface
                id="popup"
                style="left: unset;"
                bind:this={menu}
                anchorCorner="BOTTOM_LEFT"
            >
                <List>
                    <Item
                        ><Graphic class="material-icons">add</Graphic>
                        <Text>Add app</Text></Item
                    >
                    <!-- TODO: Only display when app entry is shown -->
                    <Item
                        ><Graphic class="material-icons">edit</Graphic><Text
                            >Edit this app</Text
                        ></Item
                    >
                </List>
            </MenuSurface>
        </Section>
    </Row>
</TopAppBar>

<style>
    :global(.white) {
        color: white !important;
    }
</style>
