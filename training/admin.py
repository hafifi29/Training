from django.contrib import admin
from training.models import Nominee_user,Vote,Contention

# Register your models here.

admin.site.register(Nominee_user)
admin.site.register(Vote)
admin.site.register(Contention)