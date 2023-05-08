from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import *
from django.contrib.auth.models import User


class ElectoralProgForm(forms.ModelForm):
    class Meta:
        model = electoral_prog
        fields = ['personnal_pic', 'acheivement_brief', 'program_brief', 'electoral_symbol', 'electoral_symbol_name']


class nomForm1(forms.ModelForm):
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
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")

class nomForm2(forms.ModelForm):
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
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")

class nomForm3(forms.ModelForm):
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
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")

class nomForm4(forms.ModelForm):
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
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")



class voteForm1(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الأسر')

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        super().__init__(*args, **kwargs)
        UsersinSamecollegeANDcollegeYear = User_Model.objects.filter(college = Userr.college, collegeYear = Userr.collegeYear)
        
        i=1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            visible.field.queryset = Nominee_user.objects.filter(
        community=i, UserModelKey__in = UsersinSamecollegeANDcollegeYear, final_list=True)
            i += 1

    def validate_multiple_choices(value):
        # Check if the selected options count is less than two
        if len(value) < 2:
            raise forms.ValidationError("Select at least two options.")

class voteForm2(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الأسر')

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        type = kwargs.pop('typee', None)
        if type == 'college':
            super().__init__(*args, **kwargs)
            UserModelKeyy = User_Model.objects.filter(college = Userr.college)
            i=1
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'vote-field'
                visible.field.queryset = Nominee_user.objects.filter(
            community=i, UserModelKey__in = UserModelKeyy  , final_list=True)
                i += 1

class voteForm3(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الأسر')

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        type = kwargs.pop('typee', None)
        if type == 'college':
            super().__init__(*args, **kwargs)
            UserModelKeyy = User_Model.objects.filter(college = Userr.college)
            i=1
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'vote-field'
                visible.field.queryset = Nominee_user.objects.filter(
            community=i, UserModelKey__in = UserModelKeyy  , final_list=True)
                i += 1

class voteForm4(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الأسر')

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        type = kwargs.pop('typee', None)
        if type == 'college':
            super().__init__(*args, **kwargs)
            UserModelKeyy = User_Model.objects.filter(college = Userr.college)
            i=1
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'vote-field'
                visible.field.queryset = Nominee_user.objects.filter(
            community=i, UserModelKey__in = UserModelKeyy  , final_list=True)
                i += 1


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
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")


class pickcollegerepres(forms.Form):
    union_secretary = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='أمين اتحاد')
    helper_union_secretary = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='أمين مساعد اتحاد')
    
    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        super().__init__(*args, **kwargs)
        UserModelKeyy = User_Model.objects.filter(college = Userr.college)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            
        i=1
        for community in Nominee_user._meta.get_field('community').choices:
            self.fields['union_secretary'].queryset = self.fields['union_secretary'].queryset | Nominee_user.objects.filter(
        community=i, UserModelKey__in = UserModelKeyy  , final_list=True).order_by('-collegeNumofvotes')[:1]
            
            self.fields['helper_union_secretary'].queryset = self.fields['helper_union_secretary'].queryset | Nominee_user.objects.filter(
        community=i, UserModelKey__in = UserModelKeyy  , final_list=True).order_by('-collegeNumofvotes')[1:2]
            i += 1

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
    collegevote_start_date = forms.DateTimeField(label='بداية مرحلة انتخاب الكليات',widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))

    collegevote_end_date = forms.DateTimeField(label='نهاية مرحلة انتخاب الكليات', widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))
    
    universityvote_start_date = forms.DateTimeField(label='بداية مرحلة انتخاب الجامعة',widget=forms.widgets.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
            }
        ))

    universityvote_end_date = forms.DateTimeField(label='نهاية مرحلة انتخاب الجامعة', widget=forms.widgets.DateTimeInput(
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
