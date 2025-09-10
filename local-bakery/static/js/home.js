// Show popup after 5 seconds only on home page
window.onload = function () {
    if (window.location.pathname === "/" || window.location.pathname.includes("home")) {
        setTimeout(function () {
            document.getElementById("newsletter-popup").style.display = "flex";
        }, 5000); // 5000ms = 5 seconds
    }

    // Close popup button
    document.getElementById("close-popup").onclick = function () {
        document.getElementById("newsletter-popup").style.display = "none";
    };
};
