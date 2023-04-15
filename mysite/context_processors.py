from training.models import Control_content, Admin_user
from django.contrib.auth.models import User as User

def control_content(request):
    return {'access' : Control_content.objects.first()}