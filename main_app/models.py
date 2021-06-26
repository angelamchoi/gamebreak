from django.db import models
from django.contrib.auth.models import User

#CONSTANTS
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


# Game model
class Game(models.Model):
    title = models.CharField(max_length=100)
    date = models.IntegerField()
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