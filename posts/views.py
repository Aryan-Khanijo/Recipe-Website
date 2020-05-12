from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Recipes
from . import forms


# Create your views here.
def index(request):
   return render(request, 'accounts/index.html')
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #send_mail(subject,Message,from_email,to_list,fail_silently = True)
            subject = 'verification fo account'
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
def login_view(request):
   if request.method == 'POST':
      form = AuthenticationForm(data = request.POST)
      if form.is_valid():
         username = form.cleaned_data.get('username')
         raw_password = form.cleaned_data.get('password1')
         user = form.get_user()
         login(request, user)
         if next in request.POST:
            return render(request.GET['next'])
         else:   
            return render(request,'posts/index.html')
   else:
      form = AuthenticationForm()   
   return render(request, 'accounts/login.html',{'form': form})

def logout_view(request):
   logout(request)
   return render(request,'accounts/index.html')


@login_required(login_url = 'login')
def home(request):
   return render(request,'posts/index.html')
@login_required(login_url = 'login')
def timeline(request):
   return render(request,'posts/timeline.html')
@login_required(login_url = 'login')
def about(request):
   return render(request,'posts/about.html')
@login_required(login_url = 'login')
def contact(request):
   return render(request,'posts/contact.html')
@login_required(login_url = 'login')
def recipes(request):
   recipes = Recipes.objects.all().order_by('Date')
   return render(request,'posts/recipes.html',{'recipes':recipes})

@login_required(login_url = 'login')
def Addrecipes(request):
   form = forms.Addrecipes()
   return render(request,'posts/addrecipes.html',{'form':form})
