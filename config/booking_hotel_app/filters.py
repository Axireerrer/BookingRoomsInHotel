import django_filters
from booking_hotel_app.models import Room, Booking


class RoomFilter(django_filters.FilterSet):
    min_cost_per_day = django_filters.NumberFilter(field_name='cost_per_day', lookup_expr='gte')
    max_cost_per_day = django_filters.NumberFilter(field_name='cost_per_day', lookup_expr='lte')
    min_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    max_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='lte')

    class Meta:
        model = Room
        fields = ['min_cost_per_day', 'max_cost_per_day', 'min_capacity', 'max_capacity']


class AvailableRoomFilter(django_filters.FilterSet):
    min_start_data = django_filters.DateFilter(field_name='start_data', lookup_expr='gte')
    max_end_data = django_filters.DateFilter(field_name='end_data', lookup_expr='lte')

    class Meta:
        model = Booking
        fields = ['min_start_data', 'max_end_data']
