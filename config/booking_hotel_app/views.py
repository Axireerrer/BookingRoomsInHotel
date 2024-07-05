from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from booking_hotel_app.filters import RoomFilter, AvailableRoomFilter
from booking_hotel_app.models import Room, Booking
from booking_hotel_app.permissions import AuthenticatedStuffPermission
from booking_hotel_app.serializers import (RoomSerializer, AvailableRoomSerializer,
                                           BookTheRoomByUserSerializer, BookedRoomSerializer)


class RoomApi(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = RoomFilter
    ordering_fields = ['cost_per_day', 'capacity']


class AvailableRoomApi(ModelViewSet):
    serializer_class = AvailableRoomSerializer
    queryset = Booking.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AvailableRoomFilter


class BookingRoomApi(APIView):
    permission_classes = [AuthenticatedStuffPermission]

    def patch(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookTheRoomByUserSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookedRoomApi(ListAPIView):
    serializer_class = BookedRoomSerializer

    def get_queryset(self):
        user = self.request.user
        if user and user.is_authenticated or user.is_staff:
            return Booking.objects.filter(user=user)
