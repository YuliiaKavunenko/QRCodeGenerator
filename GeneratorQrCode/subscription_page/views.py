from django.shortcuts import render

# Create your views here.
def render_subscription_page(request):
    return render(request = request, template_name = 'subscription_page/subscription_page.html')