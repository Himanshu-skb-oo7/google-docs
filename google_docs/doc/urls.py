from django.urls import path
from .views import DocListView, DocDetailView, DocCreateView, DocUpdateView

urlpatterns = [
    path('', DocListView.as_view(), name='doc-list'),
    path('create/', DocCreateView.as_view(), name='doc-create'),
    path('<uuid:pk>/', DocDetailView.as_view(), name='doc-detail'),
     path('update/<uuid:pk>/', DocUpdateView.as_view(), name='doc-update'),
]