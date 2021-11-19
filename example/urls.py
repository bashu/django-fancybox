from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="homepage.html")),
    re_path(r"^remote.html$", TemplateView.as_view(template_name="remote.html"), name="remote.html"),
]
