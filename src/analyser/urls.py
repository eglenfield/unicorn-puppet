from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^$', views.home, name='home'),
    url(r'^$', views.graph, name='graph'),
]