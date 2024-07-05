from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Room(models.Model):
    number_room = models.PositiveIntegerField()
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"The room №{self.number_room}"


class Booking(models.Model):
    start_data = models.DateField()
    end_data = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='free_rooms')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='booked_rooms', blank=True, null=True)

    def __str__(self):
        return f"Booking room {self.room.number_room}"

    def clean(self):

        equal_rooms = Booking.objects.filter(
            room=self.room,
            start_data=self.start_data,
            end_data=self.end_data,
            user=self.user
        ).exclude(pk=self.pk)

        overlapping_rooms = Booking.objects.filter(
            room=self.room,
            start_data__lte=self.end_data,
            end_data__gte=self.start_data,
            user=self.user
        ).exclude(pk=self.pk)

        if overlapping_rooms.exists():
            raise ValidationError("Can not to create room for booking with overlapping data")

        if equal_rooms.exists():
            raise ValidationError("Can not to create the same room for booking!")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
