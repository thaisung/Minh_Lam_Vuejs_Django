from django.urls import path
from api import views


urlpatterns = [

    # Thái thêm
    path("list_song_moods",views.list_song_moods),
    path('search_song', views.search_song.as_view()),
]
