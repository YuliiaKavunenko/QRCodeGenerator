from django.shortcuts import redirect, render

def render_home_page(request):
    if request.method == "POST":
        return redirect('subscription')

    return render(
        request=request,
        template_name="home_page/home_page.html",
        context={
            'is_authorizated': request.user.is_authenticated
        }
    )
