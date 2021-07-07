from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse

#CONSTANTS
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

PLATFORMS =(
    ('N', 'Nintendo'),
    ('X', 'Xbox'),
    ('P', 'PlayStation'),
    ('S', 'Steam')
)


# Systems model
class System(models.Model):
    platform = models.CharField('gaming system',
        max_length=1,
            choices=PLATFORMS,
            default=PLATFORMS[0][1]
    )
    date = models.IntegerField('version')

    def __str__(self):
        return f"{self.get_platform_display()}"

    def get_absolute_url(self):        
        return reverse('systems_detail', kwargs={'pk': self.id})
    # def get_absolute_url(self):
    #     return reverse('systems_detail', kwargs={'systems_id': self.id})

    class Meta:
        ordering =['-date']

# Game model
class Game(models.Model):
    title = models.CharField(max_length=100)
    date = models.IntegerField('release year')
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
    system = models.ForeignKey(System, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f"{self.get_mode_display()}"
        
    def get_absolute_url(self):        
        return reverse('game_detail', kwargs={'pk': self.id})
    
    class Meta:
        ordering =['title']

# photo model
class Photo(models.Model):
    url = models.CharField(max_length=200)
    key = models.CharField(max_length=200, default="Photo!")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for game_id: {self.game_id} @{self.url}"