from django import forms
from .models import Nominee_user, Vote, User_Model, Contention
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
    Scientific = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='1', final_list=True), label='الاختيار الاول اللجنة العلمية')
    Scientific2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='1', final_list=True), label='الاختيار الثاني اللجنة العلمية')
    Sports = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='2', final_list=True), label='الاختيار الاول اللجنة الرياضية')
    Sports2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='2', final_list=True), label='الاختيار الثاني اللجنة الرياضية')
    Social = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='3', final_list=True), label='الاختيار الاول اللجنة الاجتماعية')
    Social2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='3', final_list=True), label='الاختيار الثاني اللجنة الاجتماعية')
    Scout = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='4', final_list=True), label='الاختيار الاول لجنة الجوالة')
    Scout2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='4', final_list=True), label='الاختيار الثاني لجنة الجوالة')
    Cultural = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='5', final_list=True), label='الاختيار الاولاللجنة الثقافية')
    Cultural2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='5', final_list=True), label='الاختيار الثاني اللجنة الثقافية')
    Art = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='6', final_list=True), label='الاختيار الاول اللجنة الفنية')
    Art2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='6', final_list=True), label='الاختيار الثاني اللجنة الفنية')
    Family = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='7', final_list=True), label='الاختيار الاول لجنة الأسر')
    Family2 = forms.ModelChoiceField(Nominee_user.objects.filter(
        community='7', final_list=True), label='الاختيار الثاني لجنة الأسر')


class ResultForm(forms.Form):
    Nominee_id = forms.CharField(label='الكود')


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
