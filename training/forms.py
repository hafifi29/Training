from django import forms

class addNominee(forms.Form):

    nominee_id = forms.CharField(max_length=6) 
    phone_no = forms.CharField(max_length=12)
    community = forms.MultipleChoiceField(choices=['اللجنة العلمية','اللجنة الرياضية','اللجنة الاجتماعية','أسرة الجوالة و الخدمات','اللجنة الثقافية','اللجنة الفنية','لجنة الاسر و الرحلات'])
    rec_letter = forms.FileField()
    email = forms.EmailField()
