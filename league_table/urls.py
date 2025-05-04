from django.urls import path
from .views import league_table

urlpatterns = [
    path('', view=league_table, name='league_table' ),
]