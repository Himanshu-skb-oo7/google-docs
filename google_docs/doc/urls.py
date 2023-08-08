from django.urls import path
from .views import DocListView, DocDetailView

urlpatterns = [
    path('', DocListView.as_view(), name='doc-list'),
    path('<uuid:pk>/', DocDetailView.as_view(), name='doc-detail'),
]