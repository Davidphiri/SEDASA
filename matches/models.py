from django.db import models

# Create your models here.
class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.TimeField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    field = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"
    