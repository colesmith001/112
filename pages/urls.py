from django.urls import path 
from .views import HomePageView, AboutPageView, ContactPageView, CareersPageView, AdminPageView, CatalogPageView, contact_page


urlpatterns = [
  path("", HomePageView.as_view(), name="home"),
  path("about/", AboutPageView.as_view(), name="about"),
  path("catalog/", CatalogPageView.as_view(template_name="pages/catalog.html"), name="catalog"),
  path("contact/", contact_page, name="contact"),
  path("careers/", CareersPageView.as_view(template_name="pages/careers.html"), name = "careers"),
  path("admin/", AdminPageView.as_view(template_name="pages/admin.html"), name = "admin")
]

