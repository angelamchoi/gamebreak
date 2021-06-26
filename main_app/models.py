from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Constants
PLAYERS = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4+', 'Four')
)

GENRES=(
    ('A', 'Adventure'),
    ('F', 'Fighting'),
    ('I', 'Indie'),
    ('R', 'Racing'),
    ('S', 'Sport'),
    ('T', 'Tactical')
)

MODES =(
    ('M', 'Multiplayer'),
    ('S', 'Single player'),
    ('C', 'Co-operative'),
    ('B', 'Battle Royale')
)


# System model
class System(models.Model):
    name = models.CharField(max_length =250)
    release_date= models.DateField()
    num_players= models.IntegerField(
        choices=PLAYERS,
        default=PLAYERS[0][0]
    )
    gaming_platform = models.CharField(max_length=250)

# Game model
class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField('release date')
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        default=GENRES[0][0]
    )
    mode = models.CharField(
        max_length=1,
        choices=MODES,
        default=MODES[0][0]
)