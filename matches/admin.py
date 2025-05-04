from django.contrib import admin
from .models import Match
# Register your models here.
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'away_team', 'date', 'time',)
    search_fields = ('home_team', 'away_team', 'date', 'time')
    list_filter = ('date', 'time',)
    ordering = ('date', 'time')
    
    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'