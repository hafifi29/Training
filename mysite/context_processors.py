from training.models import Control_content

def control_content(request):
    return {'acess':Control_content.objects.first()}