from django.contrib import admin
from .models import Team
# Register your models here.

#Regiter the Team model with the admin site
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    
    class Meta:
        verbose_name_plural = 'Teams'
        verbose_name = 'Team'
                