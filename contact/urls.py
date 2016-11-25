from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'contact'
urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='contact/index.html'), name='index'),
    url(r'^$', views.contact, name='index'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    # url(r'^test$', views.test),
]