from django.conf.urls import  url
from . import  views
urlpatterns = [
    url(r'^$', views.pedro,name='pedro'),

]
