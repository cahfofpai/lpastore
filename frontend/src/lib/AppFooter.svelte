<script>
    import { config } from "../../app_config.js"
    import { Button, Footer } from "svelte-materialify"
    import { url } from "@roxi/routify"
</script>

<Footer class="justify-center pa-4 flex-column">
    <div class="mt-2 mb-4">
        {#each config.footer.links as link}
            <a href={$url(link.path)}
                ><Button text rounded>{link.name}</Button></a
            >
        {/each}
    </div>
    <div>
        {config.footer.copyright_notice}
    </div>
</Footer>
