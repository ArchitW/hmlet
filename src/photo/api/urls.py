from django.conf.urls import url
from .views import (
    PhotoAPIView,
    PhotoDetailAPIView,
    PhotoUpdateAPIView,
    PhotoDeleteAPIView,
)

urlpatterns = [
    url(r'^$', PhotoAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', PhotoDetailAPIView.as_view()),
    url(r'^(?P<id>\d+)/update/$', PhotoUpdateAPIView.as_view()),
    url(r'^(?P<id>\d+)/delete/$', PhotoDeleteAPIView.as_view()),
]
