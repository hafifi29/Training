
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='log_out'),
    path('nomination/', views.nomination, name='nomination'),
    path('vote/', views.vote, name='vote1'),
    path('results/', views.result, name='result'),
    path('contention/', views.contention, name='contention'),
    path('new_elections/',views.new_elections,name='new_elections'),
    path('adminp/', views.admin, name='adminp'),
    path('list_nominee/',
         views.list_nominee, name='list_nominee'),
    path('update_nominee/<nominee_id>',
         views.update_nominee, name='update_nominee'),
    path('duration/',
         views.duration, name='duration'),
    path('list_contention/',
         views.list_contention, name='list_contention'),


]
