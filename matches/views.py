from django.shortcuts import render
from .models import Match
# Create your views here.

def home(request):
    
    context = {}
    # pylint: disable=no-member
    
    context["matchset"] = Match.objects.all().order_by('-date', '-time')
    return render(request, 'sunday_league/index.html', context)