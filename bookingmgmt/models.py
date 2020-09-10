from django.db import models
from cities_light.models import SubRegion
from showmgmt.models import Show
import uuid

class Booking(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, related_name='booked_show', on_delete=models.CASCADE)
    booking_id = models.UUIDField(default=uuid.uuid4)
    reserved_seat_count = models.IntegerField(default=1)
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def __str__(self):
        return "%s - %s" % (self.show, self.user.email)


# Create your models here.
