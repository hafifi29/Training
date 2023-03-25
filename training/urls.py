
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('signin/', views.sign_in, name = 'sign_in'),
    path('nomination/', views.nomination, name = 'nomination'),
    path('vote/',views.vote,name = 'vote1'),
]
