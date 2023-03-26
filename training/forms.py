from django import forms
from .models import Nominee_user, Vote


class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee_user
        fields = [
            'Name',
            'phone_no',
            'nominee_id',
            'email',
            'birthdate',
            'address',
            'collegeYear',
            'community',
            'rec_letter',
        ]

    nominee_id = forms.CharField(max_length=6)
    phone_no = forms.CharField(max_length=12)
    community = forms.ChoiceField(choices=(('1', 'اللجنة العلمية'),
                                           ('2', 'اللجنة الرياضية'),
                                           ('3', 'اللجنة الاجتماعية'),
                                           ('4', 'أسرة الجوالة و الخدمات'),
                                           ('5', 'اللجنة الثقافية'),
                                           ('6', 'اللجنة الفنية'),
                                           ('7', 'لجنة الاسر و الرحلات')
                                           )
                                  )
    rec_letter = forms.FileField()
    email = forms.EmailField()


class VoteForm(forms.Form):

    # if Nominee_user.objects.final_list == True:
    Sports = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='الرياضية', final_list=True))
    Scientific = forms.ModelChoiceField(
        Nominee_user.objects.filter(community='العلمية', final_list=True))
    Social = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='الاجتماعية', final_list=True))
    Scout = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='أسرةالجوالة', final_list=True))
    Cultural = forms.ModelChoiceField(
        Nominee_user.objects.filter(community='الثقافية', final_list=True))
    Art = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='الفنية', final_list=True))
    Family = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='الاسر والرحلات', final_list=True))
