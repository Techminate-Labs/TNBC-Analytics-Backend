from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from v1.statistics.urls import router as statistics_router

schema_view = get_schema_view(
    openapi.Info(
        title="TNB Analytics API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('v1.statistics.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v2/', include('v2.urls')),
]

router = DefaultRouter(trailing_slash=False)
router.registry.extend(statistics_router.registry)
urlpatterns += router.urls
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
