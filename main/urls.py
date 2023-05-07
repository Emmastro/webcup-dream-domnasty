from main import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dream', views.DreamViewSet, basename='location')
router.register(r'post', views.PostViewSet, basename='post')
router.register(r'contact', views.ContactViewSet, basename='contact')
router.register(r'category', views.CategoryViewSet, basename='category')
urlpatterns = router.urls
