
from django.forms import ModelForm
from .models import System

class SystemForm(ModelForm):
    class Meta:
        model = System
        fields = ['platform']