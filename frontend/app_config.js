export let config = {
    name: "LPAStore",
    repository: "<link_to_repo>",
    menu: {
        background_color: "deep-orange lighten-1",
        text_color: "white-text",
    },
    footer: {
        copyright_notice: `C 2022 – LPAStore`,
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
    about_text: `Test\ntest`,
    contribute_text: `Test`,
    imprint_text: `Test`,
    privacy_text: `
    <b>Your privacy is very important to us</b>
    <i>...</i>
    `,
}
