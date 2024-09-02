from django.contrib import admin
from .models import Player, Club, League, Stat
from datetime import date, timedelta
import math

#Custom Filtering and search bar for each model

class PlayerAdmin(admin.ModelAdmin):
    list_display = (Player.__str__, 'player_age', 'country', 'position', 'club__club_name', 'jersey_number', 'loaned_out', 'loaned_in','profile_image')
    search_fields = [ 'player_first_name', 'player_last_name', 'position' ,'club__club_name']
    list_filter = ['club__club_name', 'position', 'country']

    def player_age(self, obj:Player) -> int:
        age = math.floor(((date.today() - obj.dob).days)/366)
        return age

class ClubAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'squad_size', 'club_country', 'league__league_name')
    search_fields = [ 'club_name', 'club_country', 'league__league_name']
    list_filter = ['league__league_name','club_country']

class LeagueAdmin(admin.ModelAdmin):
    list_display = ('league_name', 'league_country', 'max_teams','current_champion')
    search_fields = ['league_name']

class StatAdmin(admin.ModelAdmin):
    list_display = ('stat_of_player', 'appearances', 'goals', 'assists', 'clean_sheets', 'performance')
    search_fields = ['stat_of_player']

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Stat, StatAdmin)
