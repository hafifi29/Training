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
    community = forms.ChoiceField(choices = ( ('1','اللجنة العلمية'),
                                            ('2','اللجنة الرياضية'),
                                            ('3','اللجنة الاجتماعية'),
                                            ('4','أسرة الجوالة و الخدمات'),
                                            ('5','اللجنة الثقافية'),
                                            ('6','اللجنة الفنية'),
                                            ('7','لجنة الاسر و الرحلات')
                                        )
                )
    rec_letter = forms.FileField()
    email = forms.EmailField()



class VoteForm(forms.Form):
    Sports = forms.ModelChoiceField(Nominee_user.objects.filter(community='الرياضية'))
    Scientific = forms.ModelChoiceField(Nominee_user.objects.filter(community='العلمية'))
    Social = forms.ModelChoiceField(Nominee_user.objects.filter(community='الاجتماعية'))
    Scout = forms.ModelChoiceField(Nominee_user.objects.filter(community='أسرةالجوالة'))
    Cultural = forms.ModelChoiceField(Nominee_user.objects.filter(community='الثقافية'))
    Art = forms.ModelChoiceField(Nominee_user.objects.filter(community='الفنية'))
    Family = forms.ModelChoiceField(Nominee_user.objects.filter(community='الاسر والرحلات'))
