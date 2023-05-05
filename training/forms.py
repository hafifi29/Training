from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import *
from django.contrib.auth.models import User


class NomineeForm(forms.ModelForm):
    class Meta:
        model = Nominee_user
        fields = [
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
    nominee_id = forms.CharField(disabled=True, label="الكود")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(disabled=True, label="العنوان")
    birthdate = forms.DateField(disabled=True, label="تاريخ الميلاد")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")


class VoteForm(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='1', final_list=True), label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='2', final_list=True), label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='3', final_list=True), label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='4', final_list=True), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='5', final_list=True), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='6', final_list=True), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.filter(
        community='7', final_list=True), label='لجنة الأسر')

    def __init__(self, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'

    def validate_multiple_choices(value):
        # Check if the selected options count is less than two
        if len(value) < 2:
            raise forms.ValidationError("Select at least two options.")


class ContentionForm(forms.ModelForm):
    class Meta:
        model = Contention

        fields = [
            'nominee_id',
            'reason',
        ]

    Name = forms.CharField(disabled=True, label="الاسم")
    User_id = forms.CharField(disabled=True, label="الكود")
    nominee_id = forms.ModelChoiceField(
        Nominee_user.objects.filter(final_list=True), label="المرشح")
    reason = forms.Field(label="السبب")


class NomineeForm_update(forms.ModelForm):
    class Meta:
        model = Nominee_user
        fields = [
            'phone_no',
            'email',
            'community',
            'rec_letter',
            'final_list'
        ]
        labels = {
            "phone_no": "رقم الموبايل",
            'email': 'الايميل',
            'community': 'اللجنة',
            'rec_letter': 'اثبات المشاركة فى الأنشطة',
            'final_list': 'اللائحة النهائية'
        }
    nominee_id = forms.CharField(disabled=True, label="الكود")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(disabled=True, label="العنوان")
    birthdate = forms.DateField(disabled=True, label="تاريخ الميلاد")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")



# Admin Panel Forms
class Dates_form (forms.Form):
    
    nomin_start_date = forms.DateTimeField(label='بداية مرحلة التقديم',widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))

    nomin_end_date = forms.DateTimeField(label='نهاية مرحلة التقديم', widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))
    vote_start_date = forms.DateTimeField(label='بداية مرحلة الانتخاب',widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))

    vote_end_date = forms.DateTimeField(label='نهاية مرحلة الانتخاب', widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))
    con_start_date = forms.DateTimeField(label='بداية مرحلة الطعن',widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))

    con_end_date = forms.DateTimeField(label='نهاية مرحلة الطعن', widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))
    
    result = forms.BooleanField(label='اظهار النتيجة للمرشحين', required=False)
