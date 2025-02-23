from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Subscription

def render_subscription_page(request):
    if not request.user.is_authenticated:
        return redirect("authorization")  # Перенаправление, если не авторизован

    if request.method == "POST":
        new_plan = request.POST.get("plan")
        if new_plan in ["standart", "pro"]:
            request.session["new_subscription"] = new_plan
            return redirect("payment")

        elif new_plan == "free":
            subscription = Subscription.objects.get(user=request.user)
            subscription.subscription_type = "free"
            subscription.qr_limit = 1
            subscription.save()
            return redirect("subscription")

    return render(
        request,
        "subscription_page/subscription_page.html",
        {"is_authorizated": request.user.is_authenticated},
    )

def render_payment_page(request):
    if not request.user.is_authenticated:
        return redirect("authorization")  

    new_plan = request.session.get("new_subscription")
    error_message = None  

    if request.method == "POST" and new_plan:
        password = request.POST.get("password")

        # Проверяем пароль пользователя
        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            # Обновляем подписку
            subscription = Subscription.objects.get(user=request.user)
            subscription.subscription_type = new_plan
            subscription.qr_limit = 10 if new_plan == "standart" else 100
            subscription.save()

            del request.session["new_subscription"]
            return redirect("subscription")
        else:
            error_message = "Incorrect password. Please try again."

    return render(
        request, 
        "subscription_page/payment_page.html", 
        {"new_subscription": new_plan, "error_message": error_message}
    )
