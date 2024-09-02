from django.db import models

# Create your models here.
#Player model
class Player(models.Model):
    
    #player_name, country, dob, age, position, ovr, 
    # profile_image, current_club, jersey_number, 
    # player_id(primary_key)

    #primary key
    player_id = models.CharField(primary_key=True, blank=False, max_length=10)
    
    #player name
    player_first_name = models.CharField(max_length=200, blank=True, null=False)
    player_last_name = models.CharField(max_length=200, blank=False, null=False)
    
    #date of birth
    dob = models.DateField(blank=False)
    
    #country
    country = models.CharField(max_length=70, blank=False, null=False)
    
    #playable position and overall rating
    position = models.CharField(blank=False, max_length=20)
    ovr = models.PositiveIntegerField(blank=False, null=False)
    
    #profile image
    profile_image = models.ImageField(upload_to='profiles/', blank=True)
    
    #jersey number
    jersey_number = models.PositiveIntegerField(blank=True, default=999)
    
    #loan status
    loaned_out = models.BooleanField(default=False, null=False, blank=True)
    loaned_in = models.BooleanField(default=False, null=False, blank=True)

    #current club
    club = models.ForeignKey(
        to = 'Club',
        on_delete = models.SET_NULL,
        blank = False,
        null = True,
        )
    
    #statistics id
    stat = models.OneToOneField(
         to='Stat',
         on_delete= models.SET_NULL,
         blank=True,
         null=True,
    )

    def __str__(self):
        player_name = self.player_first_name + " " + self.player_last_name
        return player_name

#Club model
class Club(models.Model):
    
    #club_id, club_name, club_logo, club_league, club_country, 
    # league_position, squad_size, color_1, color_2, color_3
    
    #primary key
    club_id = models.CharField(max_length=10, primary_key=True, blank=False)
    
    #club name and logo
    club_name = models.CharField(max_length=100, blank=False, null=False)
    club_logo = models.FileField(upload_to='clubs/', blank=False)
    
    #league playing in
    league = models.ForeignKey(
        to = 'League',
        on_delete = models.SET_NULL,
        null = True,
        blank = False,
    )

    #country
    club_country = models.CharField(max_length=200, blank=False)
    
    #current position in league
    league_position = models.PositiveIntegerField(blank=False, null=False)
    
    #squad size of each team
    squad_size = models.PositiveIntegerField(blank=False, null=False)
    
    #popularity
    popularity = models.DecimalField(decimal_places=2, max_digits=3, default=5.0, blank=False, null=False)

    #club colors
    primary_color = models.CharField(max_length=7, default="#ffffff")
    secondary_color = models.CharField(max_length=7, default="#ffffff")
    
    #color for text in cards
    text_color = models.CharField(max_length=7, default="#ffffff")


    def __str__(self):
        return self.club_name

#League model    
class League(models.Model):

    #league_id, league_name, league_country, max_teams, max_alloted_squad_size
    
    #primary key
    league_id=models.CharField(max_length=10, primary_key=True, blank=False)
    
    #league name and logo
    league_name=models.CharField(max_length=100, blank=False, null=False)
    league_logo = models.ImageField(upload_to='leagues/', blank=False, null=False)
    
    #country
    league_country = models.CharField(max_length=100, blank=False, null=False)
    
    #max number of teams playing in the league
    max_teams = models.PositiveIntegerField(blank=False, null=False)
    
    #max alloted squad size of each team
    max_alloted_squad_size = models.PositiveIntegerField(blank=False, null=False)

    #current champion
    current_champion = models.CharField(null=True, blank=True, max_length=100)

    #club colors
    primary_color = models.CharField(max_length=7, default="#ffffff")
    text_color = models.CharField(max_length=7, default="#ffffff")
    
    
    def __str__(self):
        return self.league_name
    
#Stat model
class Stat(models.Model):
        #player_id(primary key), goals, assists, 
        # #clearances, clean_sheets, performance, matches_played,
        #total_minutes_played, saves
        #total_shots_taken, shots_on_target
        #total_passes_made, #successful_passes_made
        #total_tackles, successful_tackles, successful_interceptions
        #total_shots_faced

        #primary key
        stat_id = models.AutoField(primary_key=True, blank=False)
        
        #player name
        stat_of_player = models.CharField( default="player",null=False, blank=False, unique=True, max_length=100)
        
        #goals(ATK, MID, DEF) and assists(ATK, MID, DEF)
        goals = models.PositiveIntegerField(default=0, blank=True,null=False)
        assists = models.PositiveIntegerField(default=0, blank=True, null=False)
        
        #clean sheets(ALL), clearances(MID,DEF,GK) and saves(GK) 
        clean_sheets = models.PositiveIntegerField(default=0, blank=True, null=False)
        clearances = models.PositiveIntegerField(default=0, blank=True, null=False)
        saves = models.PositiveIntegerField(default=0, blank=True, null=False)
        blocks =models.PositiveIntegerField(default=0, blank=True, null=False)
        
        #performance rating(ALL)
        performance = models.FloatField(default=0.00, blank=True, null=False)
        
        #matches and total minutes played(ALL)
        appearances = models.PositiveIntegerField(default=0, blank=True, null=False)
        total_minutes = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        
        #shots taken and on target shots(ATK, MID)
        total_shots_taken = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        shots_on_target = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        
        #passes and crosses(ATK, DEF, MID)
        passes = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        crosses = models.PositiveBigIntegerField(default=0, blank=True, null=False)

        #dribbles and through bals(ATK , MID, DEF)
        successful_dribbles = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        through_balls = models.PositiveBigIntegerField(default=0, blank=True, null=False)

        
        #tackles, successfull tackles, and interceptions(MID, DEF)
        total_tackles = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        successful_tackles = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        successful_interceptions = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        
        #shots faced(GK)
        punches = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        high_claims = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        catches = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        throw_outs = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        goal_kicks = models.PositiveBigIntegerField(default=0, blank=True, null=False)
        accurate_long_balls = models.PositiveBigIntegerField(default=0, blank=True, null=False)

        #fouls and cards(ATK, DEF, MID)
        fouls_made = models.PositiveIntegerField(default=0, blank=True, null=False)
        yellow_cards = models.PositiveIntegerField(default=0, blank=True, null=False)
        red_cards = models.PositiveIntegerField(default=0, blank=True, null=False)
        
        #offside(ATK)
        offsides = models.PositiveIntegerField(default=0, blank=True, null=False)

        #penalties and freekicks(ATK, MID)
        penalties_taken = models.PositiveIntegerField(default=0, blank=True, null=False)
        penalties_scored = models.PositiveIntegerField(default=0, blank=True, null=False)
        freekicks_taken = models.PositiveIntegerField(default=0, blank=True, null=False)
        freekicks_scored = models.PositiveIntegerField(default=0, blank=True, null=False)

        #penalties saved by GK
        penalties_saved = models.PositiveIntegerField(default=0, null=False,blank=True)

        #headers and corners
        headers_won = models.PositiveIntegerField(default=0, blank=True, null=False)
        corners_taken = models.PositiveIntegerField(default=0, blank=True, null=False)

        #goals conceded(GK)
        goals_conceded = models.PositiveIntegerField(default=0, blank=True, null=False)

        #own goals(ALL
        own_goals = models.PositiveIntegerField(default=0, blank=True, null=False)


        def __str__(self):
             return "Stats of " + self.stat_of_player

     

