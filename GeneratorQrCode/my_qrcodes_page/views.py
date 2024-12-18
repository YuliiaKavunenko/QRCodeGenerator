from django.shortcuts import render

# Create your views here.

def render_myqrcodespage(request):
    return render(request=request, template_name="my_qrcodes_page/my_qrcodes_page.html")
