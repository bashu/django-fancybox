from django.conf.urls import url

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^remote.html$', TemplateView.as_view(template_name='remote.html'), name="remote.html"),
]
