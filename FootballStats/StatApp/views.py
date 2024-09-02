from django.shortcuts import render
from .custom_queries import *
# Create your views here.

#Home Page
def home_view(request):
    top_players_list = top_players()
    top_attackers_list = top_attackers()
    top_midfielders_list = top_midfielders()
    top_defenders_list = top_defenders()
    top_goalkeepers_list = top_goalkeepers()
    return render(request, 'home.html', {'player_list': top_players_list, 'attacker_list':top_attackers_list, 'midfielder_list':top_midfielders_list, 'defender_list':top_defenders_list, 'goalkeeper_list':top_goalkeepers_list})

#Player Page
def player_view(request, club_name = "Brighton & Hove Albion"):
    all_players, club_data, loaned_out_players = club_name_data(club_name)
    return render(request, 'club_data.html', {'all_players': all_players,'club_data':club_data,'loaned_outs':loaned_out_players})

#Particular Club Page
def club_id_data_view(request, club_id=""):
    all_players, club_data, loaned_outs= club_id_data(club_id = club_id)
    return render(request, 'club_data.html', {'all_players': all_players,'club_data':club_data,'loaned_outs':loaned_outs})

#League Page
def league_view(request):
    leagues = league_data()
    return render(request, 'league.html',{'leagues':leagues})

#Particular League Page
def league_data_view(request, league_id):
    all_clubs, league_data = particular_league_data(league_id = league_id)
    goals = top_stats()
    return render(request, 'league_data.html', {'all_clubs':all_clubs, 'league_data':league_data,'goals':goals})

def club_view(request):
    clubs = club_data()
    return render(request, 'club.html',{'clubs':clubs})
