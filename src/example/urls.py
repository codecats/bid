from django.conf.urls import patterns, url
from django.views.generic import TemplateView
import views

__author__ = 't'

urlpatterns = patterns('',
    url(r'^/index.html$', TemplateView.as_view(template_name="example/index.html"), name='index')
)
