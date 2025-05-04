from django.urls import path
from .views import home

urlpatterns = [
    path('matches/', view=home, name='matches'),
]