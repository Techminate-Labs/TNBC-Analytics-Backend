from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from v1.constants.urls import router as constants_router
from v1.statistics.urls import router as statistics_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chain/', include('v1.statistics.urls'))
]

router = DefaultRouter(trailing_slash=False)
router.registry.extend(constants_router.registry)
router.registry.extend(statistics_router.registry)
urlpatterns += router.urls
