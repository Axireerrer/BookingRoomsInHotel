from django.urls import path
from booking_hotel_app import views


urlpatterns = [
    path('', views.RoomApi.as_view(), name='rooms'),
    path('available/', views.AvailableRoomApi.as_view(), name='available'),
    path('booking/<int:pk>/', views.BookingRoomApi.as_view(), name='booking'),
    path('booked_rooms/', views.BookedRoomApi.as_view(), name='booked_rooms')
]

