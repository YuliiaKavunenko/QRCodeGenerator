from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def render_user_page(request):
    if request.user.is_authenticated:
        username = request.user.username
        is_authenticated = True
    else:
        username = None
        is_authenticated = False

    return render(
        request=request,
        template_name="user_page/user_page.html",
        context={
            'is_authenticated': is_authenticated,
            'username': username,
        }
    )


def render_registration_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            User.objects.create_user(username = username, email = email, password = password)
            return redirect("authorization")
        else:
            return render(request = request, template_name = "registration/registration.html", context = {"current_page": "registration"})

    return render(
        request = request,
        template_name = "registration/registration.html",
        context = {"current_page": "registration"}
    )

def render_authorization_page(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request = request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error_message = "ERROR. CHECK YOUR DATA AND TRY AGAIN LATER"

    return render(
        request=request,
        template_name="authorization/authorization.html",
        context={
            "current_page": "authorization",
            "error_message": error_message,
        }
    )

def logout_user(request):
    if request.method == "POST":
        logout(request)
    return redirect("home")