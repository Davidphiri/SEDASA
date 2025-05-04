from django.db import models

# Create your models here.
class LeagueTable(models.Model):
    '''League Table Model'''
    team_name = models.CharField(max_length=100)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_name}"