from django.shortcuts import render

# Create your views here.
def render_user_page(request):
    return render(
        request = request,
        template_name = "user_page/user_page.html",
        context = {
            'is_authorizated': 0
        }
    )

def render_registration_page(request):
    return render(
        request = request,
        template_name = "registration/registration.html"
    )

def render_authorization_page(request):
    return render(
        request = request,
        template_name = "authorization/authorization.html"
    )