from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Landing Page WEB API",
        default_version='v1',
        description="Landing Page WEB API",
        terms_of_service="https://yourco/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Private"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
        # swaggerUI
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/v1/', include('landingPage.urls')),
]
