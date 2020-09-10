from .models import Booking 
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    reserved_seat_count = serializers.IntegerField()
    class Meta:
        model = Booking
        fields = ['user', 'show', 'reserved_seat_count']

