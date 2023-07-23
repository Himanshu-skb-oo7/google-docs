from django.urls import path


from .views import DocViewSet
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path("<uuid:pk>/", DocView.as_view(), name="Doc details view"),
# ]


router = DefaultRouter()
router.register(r'', DocViewSet, basename='doc')
urlpatterns = router.urls
