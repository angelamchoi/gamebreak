from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Game, System
# from django.views.generic import ListView
from django.views.generic.edit import CreateView
# SIGN IN/UP
def home(request):
    return render(request, 'home.html')

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


#Class Based Views
class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'



class SystemCreate(CreateView):
    model = System
    fields = '__all__'
    success_url = '/systems/'

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def systems_index(request):
    systems = System.objects.all()
    return render(request, 'systems/index.html', { 'systems': systems })