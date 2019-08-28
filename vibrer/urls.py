from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vibrer.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
