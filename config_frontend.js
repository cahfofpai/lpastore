export let config = {
    name: "LPAStore",
    repository: "<link_to_repo>",
    backend: {
        url: "http://localhost:8000",
    },
    menu: {
        // color values are class names provided by Svelte Materialify
        backgroundColor: "deep-orange lighten-1",
        textColor: "white-text",
    },
    footer: {
        copyrightNotice: `C 2022 – LPAStore`,
        links: [
            { path: "/", name: "Home" },
            { path: "/apps", name: "Apps" },
            { path: "/about", name: "About" },
            { path: "/contribute", name: "Contribute" },
            { path: "/privacy", name: "Privacy" },
            { path: "/imprint", name: "Imprint" },
        ],
    },
    // TODO: Line breaks are not preserved and HTML is not rendered
    aboutText: `Test\ntest`,
    contributeText: `Test`,
    imprintText: `Test`,
    privacyText: `
    <b>Your privacy is very important to us</b>
    <i>...</i>
    `,
}
