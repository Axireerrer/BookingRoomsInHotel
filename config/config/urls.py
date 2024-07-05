from django.contrib import admin
from django.urls import path, include
from config.documentation_config import schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_framework.urls')),
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/rooms/', include('booking_hotel_app.urls')),
    path('token/jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', include('users.urls')),
]
