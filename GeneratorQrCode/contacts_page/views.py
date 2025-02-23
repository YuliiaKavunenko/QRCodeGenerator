from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def render_contacts_page(request):
    success_message = None

    if request.method == "POST":
        user_email = request.POST.get("your_email")
        feedback = request.POST.get("feedback")

        if user_email and feedback:  # Проверяем, что оба поля заполнены
            send_mail(
                subject="New Feedback from Website",
                message=f"Feedback from {user_email}:\n\n{feedback}",
                from_email=settings.DEFAULT_FROM_EMAIL,  # Укажите почту в настройках
                recipient_list=[settings.CONTACT_EMAIL],  # Email для получения отзывов
                fail_silently=False,
            )
            success_message = "Thank you! Your feedback has been sent successfully."

    return render(
        request = request, 
        template_name = "contacts_page/contacts_page.html", 
        context = {"success_message": success_message, 'is_authorizated': request.user.is_authenticated})
