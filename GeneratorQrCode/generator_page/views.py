import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QRCodes

def render_generatorpage(request):

    if request.method == "GET" and "download" in request.GET:
        qr_id = request.GET.get("download")
        try:
            qr_code = QRCodes.objects.get(id = qr_id)
            response = HttpResponse(qr_code.picture, content_type="image/png")
            response['Content-Disposition'] = f'attachment; filename = "{qr_code.name}.png"'
            return response
        except QRCodes.DoesNotExist:
            return HttpResponse("QR code not found!", status = 404)

    qr_instance = None
    download_link = None

    if request.method == "POST":

        if request.user.is_authenticated:

            action = request.POST.get("action")

            if action == "generate":
                qr_name = request.POST.get("QR-code-name")
                qr_link = request.POST.get("your-link")
                color = request.POST.get("color", "#000000")
                size = request.POST.get("size", "300")
                text_to_frame = request.POST.get("text-to-frame")

                if qr_name and qr_link:
                    try:
                        size = int(size)
                    except ValueError:
                        size = 300

                    qr_instance = QRCodes(name = qr_name, user = request.user, link = qr_link)

                    qr = qrcode.QRCode(
                        version = 1,
                        error_correction = qrcode.constants.ERROR_CORRECT_L,
                        box_size = 10,
                        border = 4,
                    )

                    qr.add_data(qr_link)
                    qr.make(fit = True)

                    img = qr.make_image(fill_color = color, back_color = "white").convert("RGB")
                    img = img.resize((size, size))

                    buffer = BytesIO()
                    img.save(buffer, format = "PNG")
                    filename = f'qr_{qr_name}.png'

                    qr_instance.picture.save(filename, ContentFile(buffer.getvalue()), save = False)
                    qr_instance.save()

                    download_link = f"?download={qr_instance.id}"

                else:
                    return HttpResponse("not all fields are filled in")

        else:
            return HttpResponse("you are not authorized")

    return render(
        request = request, 
        template_name = 'generator_page/generator_page.html', 
        context = {'qr_instance': qr_instance, 'download_link': download_link}
        )

