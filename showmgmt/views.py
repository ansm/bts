from django.shortcuts import render
from .models import Movie, Show, Cinema
from .serializers import MovieListSerializer, CinemaListSerializer
from rest_framework import generics


class MovieListView(generics.ListAPIView):
    """
    This API will return a list of all movies running in the city searched for, at that give time
    """

    serializer_class = MovieListSerializer
    def get_queryset(self):
        city_name = self.request.query_params.get("city")
        movie_ids = Show.objects.filter(cinema__city__name__iexact=city_name, active=True).values_list("movie_id")

        return Movie.objects.filter(id__in=movie_ids, active=True).order_by('name')


class CinemaListView(generics.ListAPIView):
    """
    This API will return list of all cinemas halls with all available shows and # of seats available for a specific movie searched for
    """

    serializer_class = CinemaListSerializer 
    def get_serializer_context(self):
        return {'movie_id': self.request.query_params.get('movie')}

    def get_queryset(self):
        movie_id = self.request.query_params.get("movie")
        city_name = self.request.query_params.get("city")
        try:
            movie = Movie.objects.get(id=movie_id)
        except:
            return []
        cinema_ids = Show.objects.filter(movie=movie).values_list('cinema_id')
        if not city_name:
            return Cinema.objects.filter(id__in=cinema_ids).order_by('name')
        else:
            return Cinema.objects.filter(city__name=city_name, id__in=cinema_ids).order_by('name')
