from django.conf.urls import url
from django.urls import path
from .consumers import DocConsumer

websocket_urlpatterns = [
    path("ws/doc/<id>/", DocConsumer.as_asgi()),
]