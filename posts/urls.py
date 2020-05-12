from django.urls import path
from . import views
from django import urls

urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('timeline',views.timeline),
    path('about',views.about),
    path('contact',views.contact),
    path('signup',views.signup),
    path('login',views.login_view,),
    path('recipes',views.recipes),
    path('logout',views.logout_view),
    path('addrecipes',views.Addrecipes),
]