from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
#function based views vs class based views 
class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Cole Smith"
        print(context)
        return context

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        return context

class CatalogPageView(TemplateView):
    template_name = "pages/catalog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Catalog Page"
        return context

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contact Page"
        return context

def contact_page(request):
    contact_info = {
        "name": "cole Smith",
        "address": "fake 123",
        "email": "cole.smith@example.com"
    }


    return render(request, "pages/contact.html", contact_info)

class CareersPageView(TemplateView):
    template_name = "pages/careers.html"

class AdminPageView(TemplateView):
    template_name = "pages/admin.html"



def contacts_page(request):
    return render(request, "pages/contact.html")


