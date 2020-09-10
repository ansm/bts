from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^book/', views.BookShowView.as_view(), name="book_show"),
]
