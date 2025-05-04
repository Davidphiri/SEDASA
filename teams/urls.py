from django.urls import path
from .views import teams

urlpatterns = [
    path('teams/',view=teams, name='teams')
]
