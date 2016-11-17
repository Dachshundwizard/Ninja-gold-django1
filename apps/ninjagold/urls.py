from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processgold/(?P<place>(cave)|(house)|(farm)|(casino))$', views.processgold),
    url(r'^reset$', views.reset)
]
