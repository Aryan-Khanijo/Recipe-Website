from django.urls import path
from . import views
from django import urls
from django.conf.urls import * 

urlpatterns = [
    path('',views.HomePage.as_view()),
    # # url(r'^login/$',),
    # urls(r'^sign-up/$', views.signup)
]