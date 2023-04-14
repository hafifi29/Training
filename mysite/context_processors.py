from training.models import Control_content

def control_content(request):
    return {'access' : Control_content.objects.first()}