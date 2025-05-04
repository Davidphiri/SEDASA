from django.db import models 

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField()
    founded_year = models.IntegerField()

    def __str__(self):
        return str(self.name)