

window.onload = function () {
    setTimeout(() => {
    let popup = document.createElement("div");
    popup.innerHTML = `
        <div style="
        position:fixed;
        top:0; left:0; width:100%; height:100%;
        background:rgba(0,0,0,0.8);
        display:flex; align-items:center; justify-content:center;
        z-index:2000;">
        <div style="
            background:#fff; color:#000; padding:30px; border-radius:10px;
            max-width:400px; text-align:center;">
            <h2>🎶 Subscribe to our Newsletter</h2>
            <p>Stay updated with the latest music releases!</p>
            <button onclick="this.closest('div').parentNode.remove()" 
            style="margin-top:15px; padding:10px 20px; border:none; background:#000; color:#fff; border-radius:5px; cursor:pointer;">
            Close
            </button>
        </div>
        </div>
    `;
    document.body.appendChild(popup);
    }, 5000);
}
