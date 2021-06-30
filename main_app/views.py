from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Game, System, Store
# from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView 

# SIGN IN/UP
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def systems_index(request):
    systems = System.objects.all()
    return render(request, 'systems/index.html', { 'systems': systems })

def stores_index(request):
    stores = Store.objects.all()
    return render(request, 'store/index.html', { 'stores': stores })

#Class Based Views
#GAMES
class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDetail(DetailView):
    model = Game

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    stores_game_doesnt_have = Store.objects.exclude(id__in = game.stores.all().values_list('id'))
    return render(request, 'games/detail.html', {
    'game': game, 
    'stores': stores_game_doesnt_have
})

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'


#SYSTEMS
class SystemCreate(CreateView):
    model = System
    fields = '__all__'
    success_url = '/systems/'

class SystemUpdate(UpdateView):
    model = System
    fields = '__all__'

class SystemDetail(DetailView):
    model = System

def systems_detail(request, system_id):
    system = System.objects.get(id=system_id)
    return render(request, 'systems/detail.html', { 'system': system })

class SystemDelete(DeleteView):
    model = System
    success_url = '/systems/'

# Store
class StoreCreate(CreateView):
    model = Store
    fields = '__all__'
    success_url = '/stores/'

class StoreUpdate(UpdateView):
    model = Store
    fields = '__all__'

def assoc_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.add(store_id)
    return redirect('games/detail', game_id=game_id)
