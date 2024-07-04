from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from booking_hotel_app.permissions import AuthenticatedStuffPermission
from booking_hotel_app.models import Room, Booking
from booking_hotel_app.serializers import (RoomSerializer, AvailableRoomSerializer,
                                           BookTheRoomByUserSerializer, BookedRoomSerializer)
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# API endpoint for get list rooms and filters its
class RoomApi(ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter]
    ordering_filter = ['cost_per_day', 'capacity']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('from_capacity', openapi.IN_QUERY, description="Minimum capacity",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('to_capacity', openapi.IN_QUERY, description="Maximum capacity",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('from_cost_per_day', openapi.IN_QUERY, description="Minimum cost per day",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('to_cost_per_day', openapi.IN_QUERY, description="Maximum cost per day",
                              type=openapi.TYPE_NUMBER),
        ],
    )
    def get_queryset(self):
        from_capacity = self.request.query_params.get('from_capacity')
        to_capacity = self.request.GET.get('to_capacity')
        from_cost_per_day = self.request.GET.get('from_cost_per_day')
        to_cost_per_day = self.request.GET.get('to_cost_per_day')

        filters = {}

        if from_capacity:
            filters['capacity__gte'] = from_capacity
        if to_capacity:
            filters['capacity__lte'] = to_capacity
        if from_cost_per_day:
            filters['cost_per_day__gte'] = from_cost_per_day
        if to_cost_per_day:
            filters['cost_per_day__lte'] = to_cost_per_day

        return Room.objects.filter(**filters)


# API endpoint for list available rooms for booking the user
class AvailableRoomApi(ListAPIView):
    serializer_class = AvailableRoomSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'start_data', openapi.IN_QUERY,
                description="My custom parameter",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'end_data', openapi.IN_QUERY,
                description="My custom parameter",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get_queryset(self):
        from_data = self.request.GET.get('start_data')
        to_data = self.request.GET.get('end_data')

        if from_data and to_data:
            available_rooms = Booking.objects.filter(
                start_data__gte=from_data,
                end_data__lte=to_data,
                user=None,
            )
            return available_rooms


# API endpoint for book the room and canceled also
class BookingRoomApi(APIView):
    permission_classes = [AuthenticatedStuffPermission]

    def patch(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookTheRoomByUserSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API endpoint for check booked rooms by user
class BookedRoomApi(ListAPIView):
    serializer_class = BookedRoomSerializer

    def get_queryset(self):
        user = self.request.user
        if user and user.is_authenticated or user.is_staff:
            return Booking.objects.filter(user=user)
