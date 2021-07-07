from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
# from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView 

# AWS
import uuid 
import boto3

from .models import Game, System, Photo
from .forms import GameForm

# Constant variables 
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'gamebreak'

# SIGN IN/UP
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):   
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

@login_required
def system_platform(request, sp_id):
    games = Game.objects.filter(system__id=sp_id)
    return render(request, 'games/index.html', {'games': games})

@login_required
def systems_index(request):
    systems = System.objects.all()
    return render(request, 'systems/index.html', { 'systems': systems })

#Class Based Views
#GAMES
class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'date', 'genre', 'mode']
    success_url = '/games/'

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = '__all__'

class GameDetail(LoginRequiredMixin, DetailView):
    model = Game

@login_required
def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'game_detail.html', {
        'game': game
})

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'

#SYSTEMS
class SystemCreate(LoginRequiredMixin, CreateView):
    model = System
    fields = '__all__'
    success_url = '/systems/'

class SystemUpdate(LoginRequiredMixin, UpdateView):
    model = System
    fields = '__all__'

class SystemDetail(LoginRequiredMixin, DetailView):
    model = System

@login_required
def systems_detail(request, system_id):
    system = System.objects.get(id=system_id)
    game_form=GameForm()
    return render(request, 'systems/detail.html', { 'system': system, 'game_form': game_form })

class SystemDelete(LoginRequiredMixin, DeleteView):
    model = System
    success_url = '/systems/'

# PHOTO
@login_required
def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, key=key, game_id=game_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
        return redirect (f"/games/{game_id}")

@login_required
def delete_game_photo(request, game_id):
    game_photo = Photo.objects.get(game_id=game_id)
    s3 = boto3.resource('s3')
    s3.Object(BUCKET, game_photo.key).delete()
    game_photo.delete()
    return redirect(f"/games/{game_id}")