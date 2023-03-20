from django.contrib import admin
from training.models import User,Nominee,Voting,Contention, Nominee_user

# Register your models here.

admin.site.register(User)
admin.site.register(Nominee)
admin.site.register(Voting)
admin.site.register(Contention)
admin.site.register(Nominee_user)