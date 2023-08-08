from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Doc
from .serializers import DocListSerializer, DocDetailSerializer

class DocListView(ListAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocListSerializer
    permission_classes = [IsAuthenticated]

class DocDetailView(RetrieveAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocDetailSerializer
    permission_classes = [IsAuthenticated]
