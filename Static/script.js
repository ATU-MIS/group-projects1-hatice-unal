setInterval(() => {
    const clock = document.getElementById("clock");
    if (clock) {
        clock.innerText = new Date().toLocaleTimeString();
    }
}, 1000);

document.addEventListener("submit", function (e) {
    if (e.target.classList.contains("delete-alert")) {
        if (!confirm("Delete this alert?")) {
            e.preventDefault();
        }
    }
});

function showToast(msg) {
    const t = document.createElement("div");
    t.className = "toast";
    t.innerText = msg;
    document.body.appendChild(t);

    setTimeout(() => t.remove(), 2500);
}
