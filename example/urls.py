from django.conf.urls import patterns, url

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^remote.html$', TemplateView.as_view(template_name='remote.html'), name="remote.html"),
)
