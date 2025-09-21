// Example JS: Popup on Home Page
window.addEventListener("load", function () {
    if (window.location.pathname === "/" || window.location.pathname.includes("home")) {
        setTimeout(() => {
            let popup = document.createElement("div");
            popup.className = "popup";
            popup.innerHTML = `
                <div class="popup-content">
                    <h2>Subscribe to our Newsletter</h2>
                    <p>Get the best recipes straight to your inbox!</p>
                    <button id="closePopup">Close</button>
                </div>
            `;
            document.body.appendChild(popup);

            document.getElementById("closePopup").addEventListener("click", () => {
                popup.remove();
            });
        }, 3000);
    }
});
