
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('signin/', views.sign_in, name = 'sign_in'),
    path('logout/',views.logout_view,name = 'log_out'),
    path('nomination/', views.nomination, name = 'nomination'),
    path('vote/',views.vote,name = 'vote1'),
    path('results/',views.result,name='result'),
    path('contention/', views.contention, name='contention')

]
