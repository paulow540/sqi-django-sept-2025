window.onload = function () {
    if (window.location.pathname === "/" || window.location.pathname.includes("home")) {
        // Run only on home page
        setTimeout(function () {
            alert(" Welcome to our Bakery Home Page! ");
        }, 2000); // 2 seconds delay
    }
};