
from django.forms import ModelForm
from .models import System, Game

class SystemForm(ModelForm):
    class Meta:
        model = System
        fields = ['platform']

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['mode', 'genre']