from django.db import models
from cities_light.models import SubRegion
from django.db.models import Sum


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    city = models.ForeignKey(SubRegion, related_name='subregion', on_delete=models.CASCADE)
    seat_strength = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "cinema"
        verbose_name_plural = "cinemas"
        
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = "movie"
        verbose_name_plural = "movies"

    def __str__(self):
        return self.name


class Show(models.Model):
    cinema = models.ForeignKey(Cinema, related_name='theater', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='film', on_delete=models.CASCADE)
    show_start_time = models.DateTimeField()
    show_end_time = models.DateTimeField()
    active = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "show"
        verbose_name_plural = "shows"

    def __str__(self):
        return "%s - %s - %s - %s" % (self.cinema.name, self.movie.name, self.show_start_time, self.show_end_time) 

    @property
    def seat_available(self):
        try:
            return self.cinema.seat_strength - self.booked_show.filter(active=True).aggregate(Sum('reserved_seat_count')).get('reserved_seat_count__sum')
        except:
            return self.cinema.seat_strength
