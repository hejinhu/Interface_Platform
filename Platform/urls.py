from django.conf.urls import url
from Platform import views

urlpatterns = [
    url(r'^index.html', views.index),
    url(r'^interfacesum.html', views.interfaceSum),
]
