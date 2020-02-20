from django.conf.urls import url
from .views import (
    PhotoAPIView,
    PhotoAPIDetailView,
)

urlpatterns = [
    url(r'^$', PhotoAPIView.as_view()),
    url(r'^$', PhotoAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', PhotoAPIDetailView.as_view()),
]
