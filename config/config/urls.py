from django.contrib import admin
from django.urls import path, include
from config.documentation_config import schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # url for admin access
    path('admin/', admin.site.urls),
    # url for default rest_framework auth
    path('rest-auth/', include('rest_framework.urls')),
    # url for getting documentation
    path('docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # url for getting api with rooms for booking
    path('api/v1/rooms/', include('booking_hotel_app.urls')),
    # url for getting jwt tokens for jwt authentication
    path('token/jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # url for register and session authentication
    path('users/', include('users.urls')),
]
