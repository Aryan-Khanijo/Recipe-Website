from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Create your forms here

class Addrecipes(forms.ModelForm):
    class Meta:
        model = models.Recipes
        fields = ['Title','Category','Ingredient','Steps','Image']
