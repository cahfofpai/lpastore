<script>
    import { url } from "@roxi/routify"
    import { Card, CardText } from "svelte-materialify"
    import AppAddAppButton from "../../lib/AppAddAppButton.svelte"

    import { DefaultService } from "../../lib/client"

    let apps = []

    DefaultService.getAppListAppsGet().then((response) => {
        apps = response
    })
</script>

<div class="d-flex justify-space-between">
    <h3>All apps</h3>
    <AppAddAppButton />
</div>

<br />
{#each apps as app}
    <Card outlined>
        <a href={$url("./" + app.id)} class="text-decoration-none">
            <CardText class="text--primary">
                <h4 class="mb-2">{app.name}</h4>
                {app.description}
            </CardText>
        </a>
    </Card>
    <br />
{/each}
