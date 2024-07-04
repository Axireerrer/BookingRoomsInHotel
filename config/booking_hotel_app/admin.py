from django.contrib import admin
from booking_hotel_app.models import Room, Booking


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ('number_room', 'cost_per_day', 'capacity')
    list_display_links = ('number_room', 'cost_per_day', 'capacity')
    list_filter = ('number_room', 'cost_per_day', 'capacity')


@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_data', 'end_data')
    list_display_links = ('user', 'room', 'start_data', 'end_data')
    list_filter = ('user', 'room', 'start_data', 'end_data')
