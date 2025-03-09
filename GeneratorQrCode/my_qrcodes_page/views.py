from django.shortcuts import render, redirect
from django.http import HttpResponse
from generator_page.models import QRCodes

def render_myqrcodespage(request):
    if not request.user.is_authenticated:
        
        return render(
            request,
            "my_qrcodes_page/my_qrcodes_page.html",
        )

    if request.method == "POST":
        qr_id = request.POST.get("qr_id")
        action = request.POST.get("action")

        try:
            qr_code = QRCodes.objects.get(id=qr_id, user=request.user)

            if action == "download":
                response = HttpResponse(qr_code.picture, content_type="image/png")
                response["Content-Disposition"] = f'attachment; filename="{qr_code.name}.png"'
                return response

            elif action == "delete":
                qr_code.delete()
                return redirect("myqrcodes")

        except QRCodes.DoesNotExist:
            return HttpResponse("QR code not found!", status=404)

    user_qrcodes = QRCodes.objects.filter(user = request.user)
    
    sort_order = request.GET.get("sort", "default")  

    if sort_order == "asc":
        user_qrcodes = QRCodes.objects.filter(user=request.user).order_by("date")
    else:
        user_qrcodes = QRCodes.objects.filter(user=request.user).order_by("-date")

    return render(
        request,
        "my_qrcodes_page/my_qrcodes_page.html",
        {
            "user_qrcodes": user_qrcodes,
            'is_authorizated': request.user.is_authenticated,
        },
    )
