from django.shortcuts import render
from matches.models import Match
from .models import LeagueTable

# Create your views here.
def league_table(request):
    # pylint: disable=no-member
    context = {}
     
    context["dataset"] = LeagueTable.objects.all().order_by('-points', '-goal_difference')
    context["matchset"] = Match.objects.all().order_by('-date')
    return render(request, 'sunday_league/index.html', context)
