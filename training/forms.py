from django import forms
from .models import Nominee_user, Vote, User_Model
from django.contrib.auth.models import User


class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee_user
        fields = [
            'nominee_id',
            'phone_no',
            'email',
            'community',
            'rec_letter',
        ]
        labels = {
        "phone_no": "رقم الموبايل",
        'email': 'الايميل',
        'community': 'اللجنة',
        'rec_letter': 'اثبات المشاركة فى الأنشطة'
    }
    
    Name = forms.CharField(disabled=True, label="الاسم")
    nominee_id = forms.CharField(disabled=True, max_length=6,label="الكود")
    address = forms.CharField(disabled=True,label="العنوان")
    birthdate = forms.DateField(disabled=True,label="تاريخ الميلاد")
    collegeYear = forms.IntegerField(disabled=True,label="الفرقة")

class VoteForm(forms.Form):

    Sports = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='2', final_list=True))
    Scientific = forms.ModelChoiceField(
        Nominee_user.objects.filter(community='1', final_list=True))
    Social = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='3', final_list=True))
    Scout = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='4', final_list=True))
    Cultural = forms.ModelChoiceField(
        Nominee_user.objects.filter(community='5', final_list=True))
    Art = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='6', final_list=True))
    Family = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='7', final_list=True))
    
class ResultForm(forms.Form):
    Nominee_id = forms.CharField()