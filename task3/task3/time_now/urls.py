from django.conf.urls import include, url
from .views import show_time

urlpatterns = [
    url(r'^$', show_time),
]
