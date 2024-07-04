from django.urls import path
from users import views

# URL for registration user
urlpatterns = [
    path('register/', views.RegisterUserApi.as_view(), name='register'),
]
