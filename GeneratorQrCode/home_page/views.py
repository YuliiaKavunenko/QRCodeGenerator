from django.shortcuts import render

# Create your views here.
def render_home_page(request):
    return render(
        request=request,
        template_name="home_page/home_page.html",
        context={
            'is_authorizated': request.user.is_authenticated
        }
    )
