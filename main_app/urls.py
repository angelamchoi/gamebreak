from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/', views.games_index, name='index'),
    path('systems/', views.systems_index, name='index'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
]
