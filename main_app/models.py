from django.db import models
from django.contrib.auth.models import User

# Constants
PLAYERS = (
    ('1', 'One'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4+', 'Four')
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
