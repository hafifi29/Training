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
    
    Name = forms.CharField(disabled=True)
"""     nominee_id = forms.CharField(initial=UserModel.objects.get().Student_id,disabled=True, max_length=6)
    address = forms.CharField(initial=UserModel.objects.get().address,disabled=True)
    birthdate = forms.DateField(initial=UserModel.objects.get().birthdate,disabled=True)
    collegeYear = forms.IntegerField(initial=UserModel.objects.get().collegeYear,disabled=True) """

class VoteForm(forms.Form):

    # if Nominee_user.objects.final_list == True:
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