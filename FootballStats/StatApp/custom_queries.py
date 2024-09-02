from .models import Player, Club, League, Stat
from django.db.models import Subquery, Q

#top_players
def top_players():
    #players_list = Player.objects.filter(stat__performance__gte = 8.5, stat__matches_played__gte = 5).order_by('-stat__performance')[:3]
    player_list = Player.objects.filter(stat__goals__gte = 0).order_by('-stat__performance')[:3]
    return player_list

#top_attackers
def top_attackers():
    player_list = Player.objects.filter(position = 'Attacker').order_by('-stat__performance', '-stat__goals')[:3]
    return player_list

#top_midfielders
def top_midfielders():
    player_list = Player.objects.filter(position = 'Midfielder').order_by('-stat__performance', '-stat__assists','-stat__passes','-stat__crosses')[:3]
    return player_list

#top_defenders
def top_defenders():
    player_list = Player.objects.filter(position = 'Defender').order_by('-stat__performance', '-stat__clearances','-stat__successful_interceptions','-stat__successful_tackles', 'stat__yellow_cards','stat__red_cards')[:3]
    return player_list

#top_goalkeepers
def top_goalkeepers():
    player_list = Player.objects.filter(position = 'Goalkeeper').order_by('-stat__performance', '-stat__clean_sheets','-stat__saves','-stat__clearances','stat__goals_conceded')[:3]
    return player_list

#all_players_of_club
def club_id_data(club_id=""):
    club = Club.objects.filter(club_id=club_id)
    club_players = Player.objects.filter(club__club_id=club_id, loaned_out=False)
    loaned_out = Player.objects.filter(club__club_id=club_id, loaned_out=True)
    criteria_1 = Q(player_first_name__in=Subquery(loaned_out.values('player_first_name')))
    criteria_2 = Q(player_last_name__in=Subquery(loaned_out.values('player_last_name')))
    criteria_3 = Q(loaned_in = True)
    loaned_out_players = Player.objects.filter(criteria_1 & criteria_2 & criteria_3).exclude(club__club_id = club_id)
    return (club_players, club, loaned_out_players)

#all_players_of_club
def club_name_data(club_name=""):
    club = Club.objects.filter(club_name=club_name)
    club_players = Player.objects.filter(club__club_name=club_name, loaned_out=False)
    loaned_out = Player.objects.filter(club__club_name=club_name, loaned_out=True)
    criteria_1 = Q(player_first_name__in=Subquery(loaned_out.values('player_first_name')))
    criteria_2 = Q(player_last_name__in=Subquery(loaned_out.values('player_last_name')))
    criteria_3 = Q(loaned_in = True)
    loaned_out_players = Player.objects.filter(criteria_1 & criteria_2 & criteria_3).exclude(club__club_name = club_name)
    return (club_players, club, loaned_out_players)

#particular league data
def particular_league_data(league_id = ""):
    league_data = League.objects.filter(league_id = league_id)
    all_clubs = Club.objects.filter(league__league_id = league_id).order_by('-popularity')
    return (all_clubs, league_data)

#club data
def club_data():
    clubs = Club.objects.filter(popularity__gte = 7.5).order_by('-popularity','league_position')[:8]
    return clubs

#league data
def league_data():
    leagues = League.objects.all().order_by('max_teams')
    return leagues

#top goals, assists, clean sheets, yellow, red
def top_stats():
    goals = Stat.objects.all().values('stat_of_player','goals').order_by('-goals')[:10]
    return goals