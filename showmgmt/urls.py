from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^movie/list/', views.MovieListView.as_view(), name="movie_list"),
    re_path(r'^cinema/list/', views.CinemaListView.as_view(), name="cinema_list"),
]

