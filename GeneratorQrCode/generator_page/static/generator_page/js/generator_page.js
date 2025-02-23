document.getElementById("go-to-design").addEventListener("click", function (event) {
    event.preventDefault();

    let qrCodeName = document.getElementById("QR-code-name").value;
    let yourLink = document.getElementById("your-link").value;

    // Устанавливаем скрытые поля для отправки
    document.getElementById("hidden-QR-code-name").value = qrCodeName;
    document.getElementById("hidden-your-link").value = yourLink;

    // Показываем базовый QR-код в `QR-code-frame-design`
    let qrContainer = document.getElementById("QR-code-frame-design");
    qrContainer.innerHTML = ""; // Очищаем контейнер

    let qrCanvas = document.createElement("canvas");
    qrCanvas.id = "qr-canvas";
    qrCanvas.width = 300;
    qrCanvas.height = 300;
    qrContainer.appendChild(qrCanvas);

    let ctx = qrCanvas.getContext("2d");
    let qrImage = new Image();
    qrImage.src = `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(yourLink)}&size=300x300`;

    qrImage.onload = function () {
        ctx.drawImage(qrImage, 0, 0, 300, 300);
    };

    // Скроллим к блоку дизайна
    document.getElementById("qr-wrapper-design").scrollIntoView({ behavior: "smooth" });
});

function updateQRCode() {
    let qrContainer = document.getElementById("QR-code-frame-design");

    // Очищаем контейнер перед добавлением нового QR-кода
    qrContainer.innerHTML = "";

    // Получаем значения для кастомизации
    let color = document.getElementById("color").value;
    let size = parseInt(document.getElementById("size").value) || 300;
    let textToFrame = document.getElementById("text-to-frame").value;
    let selectedShape = document.querySelector('input[name="shape"]:checked').value;
    let qrLink = document.getElementById("your-link").value;

    // Генерация QR-кода с учетом белого отступа
    let qr = new QRCodeStyling({
        width: size,
        height: size,
        data: qrLink,
        dotsOptions: {
            color: color,
            type: selectedShape
        },
        backgroundOptions: {
            color: "#ffffff",
            margin: 30  // Отступ белых краев по 30px
        },
        imageOptions: {
            hideBackgroundDots: true
        }
    });

    // Добавляем QR-код в контейнер
    qr.append(qrContainer);

    // Если есть текст, добавляем его под QR-код
    if (textToFrame) {
        let textElement = document.createElement("div");
        textElement.textContent = textToFrame;

        // Стили для центрирования и отступа вниз
        textElement.style.textAlign = "center";
        textElement.style.fontFamily = "Josefin Sans";
        textElement.style.fontSize = "68px";
        textElement.style.color = color;
        textElement.style.marginTop = "15px";  // Отступ вниз
        textElement.style.transform = "translateX(-50%)";
        textElement.style.position = "relative";
        textElement.style.left = "50%";

        qrContainer.appendChild(textElement);
    };
};
