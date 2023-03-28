from django.contrib import admin
from training.models import Nominee_user,Vote,Contention, User_Model,Control_content

# Register your models here.

admin.site.register(Nominee_user)
admin.site.register(Vote)
admin.site.register(Contention)
admin.site.register(User_Model)
admin.site.register(Control_content)