from django.contrib import admin
from .models import LeagueTable
# Register your models here.
@admin.register(LeagueTable)
class Table(admin.ModelAdmin):
    list_display = ('team_name', 'played', 'won', 'drawn', 'lost', 'goal_difference', 'points')
    search_fields = ('team_name',)
    list_filter = ('points',)
    ordering = ('-points',)