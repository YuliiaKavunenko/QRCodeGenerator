from django.shortcuts import render

# Create your views here.
def render_contacts_page(request):
    return render(request = request, template_name = 'contacts_page/contacts_page.html')