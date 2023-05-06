from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dream', views.DreamViewSet, basename='location')


urlpatterns = router.urls
