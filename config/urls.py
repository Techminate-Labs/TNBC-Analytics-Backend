from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from v1.constants.urls import router as constants_router

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = DefaultRouter(trailing_slash=False)
router.registry.extend(constants_router.registry)
urlpatterns += router.urls
