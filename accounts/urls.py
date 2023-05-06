#from . import views
#from rest_framework.routers import DefaultRouter
from django.urls import include, path


urlpatterns = [
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/', include('dj_rest_auth.registration.urls'))
]

