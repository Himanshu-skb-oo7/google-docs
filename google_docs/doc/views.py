from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from doc.permissions import IsOwnerOrShared

from .models import Doc
from .serializers import DocListSerializer, DocDetailSerializer, DocCreateSerializer, DocUpdateSerializer

class DocListView(ListAPIView):
    serializer_class = DocListSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrShared]

    def get_queryset(self):
        user = self.request.user 
        return Doc.objects.visible_to_user(user)
    

class DocCreateView(CreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DocUpdateView(UpdateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocUpdateSerializer
    permission_classes = [IsAuthenticated]


class DocDetailView(RetrieveAPIView):
    serializer_class = DocDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrShared]

    def get_queryset(self):
        user = self.request.user
        return Doc.objects.visible_to_user(user)
