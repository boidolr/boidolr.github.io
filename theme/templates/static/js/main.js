(function() {
    const main = {
        _scheme: "auto",
        applyScheme() {
            document.querySelector("html").setAttribute("data-theme", this.scheme);
            const e = document.querySelectorAll(this.buttonsTarget);
            e.forEach(e=>{
                const t = "dark" == this.scheme ? this.change.dark : this.change.light;
                e.innerHTML = t,
                e.setAttribute("aria-label", t.replace(/<[^>]*>?/gm, ""))
            }
            )
        },
        get preferedColorScheme() {
            return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"
        },
    };
})();