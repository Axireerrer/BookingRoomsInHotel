from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.RegisterUserApi.as_view(), name='register'),
]
