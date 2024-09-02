from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('player', views.player_view, name='player'),
    path('club', views.club_view, name='club'),
    path('particularclub/<str:club_id>', views.club_id_data_view, name="clubdata"),
    path('league', views.league_view, name='league'),
    path('particularleague/<str:league_id>', views.league_data_view, name="leaguedata"),

]
