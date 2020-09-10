from .models import Movie, Show, Cinema
from rest_framework import serializers


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name',]


class ShowListSerializer(serializers.ModelSerializer):
    seat_available = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ['id', 'show_start_time', 'show_end_time', 'seat_available']

    def get_seat_available(self, obj):
        return obj.seat_available

class CinemaListSerializer(serializers.ModelSerializer):
    shows = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'movie', 'shows']

    def get_shows(self, obj):
        try:
            return ShowListSerializer(obj.theater.filter(movie_id=self.context.get('movie_id'), active=True), many=True).data
        except:
            return []
    
    def get_movie(self, obj):
        try:
            return Movie.objects.get(id=self.context.get('movie_id')).name
        except:
            return ''
