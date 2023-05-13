from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.validators import FileExtensionValidator


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

class nomForm2(forms.Form):
    nominee_id = forms.CharField(disabled=True, label="الكود")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(disabled=True, label="العنوان")
    birthdate = forms.DateField(disabled=True, label="تاريخ الميلاد")
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")
    phone_no = forms.IntegerField(disabled=True,label = "رقم الموبايل")
    email = forms.EmailField(disabled=True, label = 'الايميل')
    community = forms.CharField(disabled=True, label = 'اللجنة')
    rec_letter = forms.FileField(disabled=True, label = 'اثبات المشاركة فى الأنشطة')

class nomForm3(forms.Form):

    nominee_id = forms.CharField(disabled=True, label="الكود")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(disabled=True, label="العنوان")
    birthdate = forms.DateField(disabled=True, label="تاريخ الميلاد")
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")
    phone_no = forms.IntegerField(disabled=True,label = "رقم الموبايل")
    email = forms.EmailField(disabled=True, label = 'الايميل')
    community = forms.CharField(disabled=True, label = 'اللجنة')
    rec_letter = forms.FileField(disabled=True, label = 'اثبات المشاركة فى الأنشطة')

class nomForm4(forms.Form):
    nominee_id = forms.CharField(disabled=True, label="الكود")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(disabled=True, label="العنوان")
    birthdate = forms.DateField(disabled=True, label="تاريخ الميلاد")
    college = forms.CharField(disabled=True, label="الكلية")
    collegeYear = forms.IntegerField(disabled=True, label="الفرقة")
    phone_no = forms.IntegerField(disabled=True,label = "رقم الموبايل")
    email = forms.EmailField(disabled=True, label = 'الايميل')
    community = forms.CharField(disabled=True, label = 'اللجنة')
    rec_letter = forms.FileField(disabled=True, label = 'اثبات المشاركة فى الأنشطة')
    nominateAs = forms.CharField(disabled=True, label = "الترشح لمنصب")


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
        community=i, UserModelKey__in = UsersinSamecollegeANDcollegeYear, communityMemberElections = True, final_list=True)
            i += 1

    def validate_multiple_choices(value):
        # Check if the selected options count is less than two
        if len(value) < 2:
            raise forms.ValidationError("Select at least two options.")

class voteForm2(forms.Form):
    collegeCommunityTrusteeNominee = forms.CharField(label='أمين اللجنة', disabled = True)
    collegeCommunityTrusteeHelperNominee = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='مساعد الأمين')
    
    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        super().__init__(*args, **kwargs)
        UsersinSamecollege = User_Model.objects.filter(college = Userr.college)
        i=1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            i += 1
        self.fields['collegeCommunityTrusteeHelperNominee'].queryset = Nominee_user.objects.filter(
    community=Nominee_user.objects.get(UserModelKey=Userr).community, UserModelKey__in = UsersinSamecollege, role = '2', collegeCommunityTrusteeOreHelperElections = True  , final_list=True)


class voteForm3(forms.Form):
    collegeStudentUnionPresidentOrVice = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='المرشح لرئيس/نائب رئيس الاتحاد')
    
    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        super().__init__(*args, **kwargs)
        UsersinSamecollege = User_Model.objects.filter(college = Userr.college)
        i=1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            i += 1
        self.fields['collegeStudentUnionPresidentOrVice'].queryset = Nominee_user.objects.filter(Q(role = '3') | Q(role = '4'),
    UserModelKey__in = UsersinSamecollege, collegeStudentUnionPresidentOrViceElections = True  , final_list=True)

class voteForm4(forms.Form):
    Scientific = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة العلمية')
    Sports = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الرياضية')
    Social = forms.ModelMultipleChoiceField(Nominee_user.objects.none(),label='اللجنة الاجتماعية')
    Scout = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الجوالة')
    Cultural = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الثقافية')
    Art = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='اللجنة الفنية')
    Family = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='لجنة الأسر')
    universityStudentUnionPresidentOrVice = forms.ModelMultipleChoiceField(Nominee_user.objects.none(), label='رئيس/نائب انحاد')

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        super().__init__(*args, **kwargs)
        UsersinSamecollegeANDcollegeYear = User_Model.objects.filter(college = Userr.college, collegeYear = Userr.collegeYear)
        


        
        i=1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            if i != 8:
                visible.field.queryset = Nominee_user.objects.filter(
            community=i, UserModelKey__in = UsersinSamecollegeANDcollegeYear, universityElections = True, final_list=True)
            else:
                visible.field.queryset = Nominee_user.objects.filter(Q(role = '5') | Q(role = '6'), universityElections = True, final_list=True)
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
        Nominee_user.objects.none(), label="المرشح")
    reason = forms.Field(label="السبب")

    def __init__(self, *args, **kwargs):
        Userr = kwargs.pop('Userr', None)
        nom = kwargs.pop('nom', None)
        super().__init__(*args, **kwargs)
        UsersinSamecollegeANDcollegeYear = User_Model.objects.filter(college = Userr.college, collegeYear = Userr.collegeYear)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'vote-field'
            visible.field.queryset = Nominee_user.objects.filter(
        community=nom.community, UserModelKey__in = UsersinSamecollegeANDcollegeYear)


class NomineeForm_update(forms.ModelForm):
    class Meta:
        model = Nominee_user
        fields = [
            'phone_no',
            'email',
            'community',
            'rec_letter',
            'final_list',
            'role',  
        ]
        labels = {
            "phone_no": "رقم الموبايل",
            'email': 'الايميل',
            'community': 'اللجنة',
            'rec_letter': 'اثبات المشاركة فى الأنشطة',
            'final_list': 'اللائحة النهائية',
            'role':'الدور'
        }
    nominee_id = forms.IntegerField(disabled=True, label="الكود")
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
class Dates_form (forms.ModelForm):
    class Meta:
        model = Dates
        fields = '__all__'
        labels = {
            "communityMemberElections_sd": "بداية مرحلة الترشح",
            "communityMemberElections_ed": "نهاية مرحلة الترشح",

            "collegeCommunityTrusteeOreHelperElections_sd": "بداية مرحلة الترشح",
            "collegeCommunityTrusteeOreHelperElections_ed": "نهاية مرحلة الترشح",

            "collegeStudentUnionPresidentOrViceElections_sd": "بداية مرحلة الترشح",
            "collegeStudentUnionPresidentOrViceElections_ed": "نهاية مرحلة الترشح",

            "universityElections_sd": "بداية مرحلة الترشح",
            "universityElections_ed": "نهاية مرحلة الترشح",

            "Voting_1_sd": "بداية مرحلة الانتخاب",
            "Voting_1_ed": "نهاية مرحلة الانتخاب",

            "Voting_2_sd": "بداية مرحلة الانتخاب",
            "Voting_2_ed": "نهاية مرحلة الانتخاب",

            "Voting_3_sd": "بداية مرحلة الانتخاب",
            "Voting_3_ed": "نهاية مرحلة الانتخاب",

            "Voting_4_sd": "بداية مرحلة الانتخاب",
            "Voting_4_ed": "نهاية مرحلة الانتخاب",

            "result_1_sd": "بداية النتيجة",
            "result_1_ed": "نهاية النتيجة",

            "result_2_sd": "بداية النتيجة",
            "result_2_ed": "نهاية النتيجة",
    
            "result_3_sd": "بداية النتيجة",
            "result_3_ed": "نهاية النتيجة",

            "result_4_sd": "بداية النتيجة",
            "result_4_ed": "نهاية النتيجة",

            "con_sd": "بداية مرحلة الطعن",
            "con_ed": "نهاية مرحلة الطعن",

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget = forms.widgets.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'min':datetime.now().strftime('%Y-%m-%dT%H:%M')
        })

#Multi file upload
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class loadData(forms.Form):
    datafile = forms.FileField(label = "اختيار الملف", validators=[FileExtensionValidator(['xlsx'], message='يرجى اختيار ملف Excel')])
    my_files = MultipleFileField(label = "اختيار ملفات اثبات المشاركة فى الأنشطة", validators=[FileExtensionValidator(['jpg', 'jpeg','png','webp'])])
                                                                                                
