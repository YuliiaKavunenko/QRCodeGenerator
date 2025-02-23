import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import QRCodes
from PIL import Image, ImageDraw
from PIL import ImageFont

def render_generatorpage(request):
    if request.method == "GET" and "download" in request.GET:
        qr_id = request.GET.get("download")
        try:
            qr_code = QRCodes.objects.get(id=qr_id)
            response = HttpResponse(qr_code.picture, content_type="image/png")
            response['Content-Disposition'] = f'attachment; filename="{qr_code.name}.png"'
            return response
        except QRCodes.DoesNotExist:
            return HttpResponse("QR code not found!", status=404)

    qr_instance = None
    download_link = None

    if request.method == "POST" and request.user.is_authenticated:
        action = request.POST.get("action")
        if action == "generate":
            qr_name = request.POST.get("QR-code-name")
            qr_link = request.POST.get("your-link")
            color = request.POST.get("color", "#000000")
            size = request.POST.get("size", "300")
            shape = request.POST.get("shape", "standard")
            text_to_frame = request.POST.get("text-to-frame", "")

            if qr_name and qr_link:
                try:
                    size = int(size)
                except ValueError:
                    size = 300

                qr_instance = QRCodes(name=qr_name, user=request.user, link=qr_link)

                qr = qrcode.QRCode(
                    version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_L,
                    box_size = 10,
                    border = 4,
                )
                qr.add_data(qr_link)
                qr.make(fit = True)

                qr_matrix = qr.modules

                img_size = size + 60
                img = Image.new("RGB", (img_size, img_size), "white")
                draw = ImageDraw.Draw(img)
                box_size = size // len(qr_matrix)

                offset_x = (img_size - len(qr_matrix) * box_size) // 2
                offset_y = (img_size - len(qr_matrix) * box_size) // 2

                for y in range(len(qr_matrix)):
                    for x in range(len(qr_matrix[y])):
                        if qr_matrix[y][x]:
                            x_pos = x * box_size + offset_x
                            y_pos = y * box_size + offset_y

                            if shape == "shape1":
                                draw.ellipse([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)
                            elif shape == "shape2":
                                draw.regular_polygon(
                                    (x_pos + box_size // 2, y_pos + box_size // 2, box_size // 2), 
                                    n_sides=5, 
                                    fill=color
                                )
                            elif shape == "shape3":
                                draw.ellipse([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)
                            elif shape == "shape4":
                                draw.polygon(
                                    [
                                        (x_pos + box_size // 2, y_pos),
                                        (x_pos + box_size, y_pos + box_size // 2),
                                        (x_pos + box_size // 2, y_pos + box_size),
                                        (x_pos, y_pos + box_size // 2),
                                    ],
                                    fill=color,
                                )
                            else:
                                draw.rectangle([(x_pos, y_pos), (x_pos + box_size, y_pos + box_size)], fill=color)

                if text_to_frame:
                    try:
                        font = ImageFont.truetype("JosefinSans-Bold.ttf", size // 2)
                    except IOError:
                        font = ImageFont.load_default()


                    bbox = draw.textbbox((0, 0), text_to_frame, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    text_x = (img_size - text_width) // 2
                    text_y = img_size - text_height - 15

                    draw.text((text_x, text_y), text_to_frame, font=font, fill=color)

                buffer = BytesIO()
                img.save(buffer, format="PNG")
                filename = f'qr_{qr_name}.png'

                qr_instance.picture.save(filename, ContentFile(buffer.getvalue()), save=False)
                qr_instance.save()

                download_link = f"?download={qr_instance.id}"

            else:
                return HttpResponse("Not all fields are filled in")
    
    return render(
        request=request,
        template_name='generator_page/generator_page.html',
        context={'qr_instance': qr_instance, 'download_link': download_link}
    )
