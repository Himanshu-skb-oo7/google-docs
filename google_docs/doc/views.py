from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import DocSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import F

from .models import Doc


class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer