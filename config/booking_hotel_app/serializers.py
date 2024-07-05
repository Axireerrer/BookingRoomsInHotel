from rest_framework import serializers
from django.contrib.auth.models import User
from booking_hotel_app.models import Room, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        ref_name = 'UserSerializer'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number_room', 'cost_per_day', 'capacity']


class AvailableRoomSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'start_data', 'end_data', 'room']


class BookTheRoomByUserSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'start_data', 'end_data', 'room']

    def validate_user(self, value):
        if value is None:
            return value

        if self.instance and self.instance.user != value:
            raise serializers.ValidationError("You can only book a room for yourself.")
        return value

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class BookedRoomSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'start_data', 'end_data']
        extra_kwargs = {
            'id': {'read_only': True},
            'start_data': {'read_only': True},
            'end_data': {'read_only': True}
        }
