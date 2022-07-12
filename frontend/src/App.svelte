<script>
    import "@smui/common"
    import Button from "@smui/button"

    let count = 0
    const increment = () => {
        count += 1
    }
</script>

<main>
    <h3>Welcome to the LPAStore!</h3>

    <h4>It features <b>{count}</b> apps for GNU/Linux on phones</h4>

    <Button on:click={increment}>Add app</Button>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        margin: 0 auto;
    }
</style>
