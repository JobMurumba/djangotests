from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf.urls import url


app_name="whatever"
urlpatterns = [
    path('list/',views.whatever,name="thelist"),
    url(r'^$',TemplateView.as_view(template_name='gethome.html'),name="home"),
    path('add/',views.add,name="add")
]