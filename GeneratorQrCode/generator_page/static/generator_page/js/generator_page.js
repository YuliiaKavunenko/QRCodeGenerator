document.getElementById("go-to-design").addEventListener("click", function(event) {
    event.preventDefault();
    let qrCodeName = document.getElementById("QR-code-name").value;
    let yourLink = document.getElementById("your-link").value;
    
    document.getElementById("hidden-QR-code-name").value = qrCodeName;
    document.getElementById("hidden-your-link").value = yourLink;
    
    document.getElementById("qr-wrapper-design").scrollIntoView({ behavior: "smooth" });
});