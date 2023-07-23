from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import DocSerializer
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Doc


class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    # def retrieve(self, request, pk=None):
    #     queryset = Doc.objects.all()
    #     doc = get_object_or_404(queryset, pk=pk)
    #     serializer = DocSerializer(doc)
    #     return Response(serializer.data)
    
    # def update(self, request, pk=None):
    #     queryset = Doc.objects.all()
    #     instance = self.get_object()
    #     data = {
    #         "content": request.PUT.get('content', None),
    #         }
    #     serializer = self.serializer_class(instance=instance,
    #                                        data=data, # or request.data
    #                                        context={'author': user},
    #                                        partial=True)
        
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)