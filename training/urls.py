
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='log_out'),

    path('nomination/<type>', views.nomination, name='nomination'),

    path('vote/<type>', views.vote, name='vote1'),

    path('results/<type>', views.showresult, name='result'),

    path('contention/', views.contention, name='contention'),
    path('new_elections/',views.new_elections,name='new_elections'),
    path('adminp/', views.admin, name='adminp'),
     path('picksec/', views.picksec, name='picksec'),
    path('list_nominee/',
         views.list_nominee, name='list_nominee'),
    path('update_nominee/<nominee_id>',
         views.update_nominee, name='update_nominee'),
    path('duration/',
         views.duration, name='duration'),
    path('list_contention/',
         views.list_contention, name='list_contention'),

     path('result_control/',
           views.result_control , name = "result_control"),
     path('update_nominee_result/<nominee_id>',
          views.update_nominee_result,name = "update_nominee_result"),
    path('particular_nominee_prog/<int:id>/', views.particular_nominee_prog, name='particular_nominee_prog'),

    path('elctoral_program/',views.electoral_program,name='elctoral_program'),
    path('nominees_programs/',views.electoral_prog_show,name='nominees_programs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
