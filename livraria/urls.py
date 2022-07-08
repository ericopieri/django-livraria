from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from core.views import CategoriaViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
