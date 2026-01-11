document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("button_theme");
    const body = document.body;

    if (localStorage.getItem("theme") === "light") {
        body.classList.add("light");
        toggle.textContent = "🌙";
    } else {
        toggle.textContent = "☀️";
    }

    toggle.addEventListener("click", () => {
        body.classList.toggle("light");

        if (body.classList.contains("light")) {
            localStorage.setItem("theme", "light");
            toggle.textContent = "🌙";
        } else {
            localStorage.setItem("theme", "dark");
            toggle.textContent = "☀️";
        }
    });
});
