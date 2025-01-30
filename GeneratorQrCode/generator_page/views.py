from django.shortcuts import render

# Create your views here.

def render_generatorpage(request):
    return render(request=request, template_name="generator_page/generator_page.html")
