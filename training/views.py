from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .forms import *
from django.contrib.auth.models import User as User_
from .models import *
from datetime import datetime
from django.utils import timezone
from django.db.models import Q
import os
import pandas as pd
from django.core.files import File
import random

# global varables
std_access = Control_content.objects.first()
dates = Dates.objects.first()

communityMemberElections_sd = dates.communityMemberElections_sd
communityMemberElections_ed = dates.communityMemberElections_ed

collegeCommunityTrusteeOreHelperElections_sd = dates.collegeCommunityTrusteeOreHelperElections_sd
collegeCommunityTrusteeOreHelperElections_ed = dates.collegeCommunityTrusteeOreHelperElections_ed

collegeStudentUnionPresidentOrViceElections_sd = dates.collegeStudentUnionPresidentOrViceElections_sd
collegeStudentUnionPresidentOrViceElections_ed = dates.collegeStudentUnionPresidentOrViceElections_ed

universityElections_sd = dates.universityElections_sd
universityElections_ed = dates.universityElections_ed


Voting_1_sd = dates.Voting_1_sd
Voting_1_ed = dates.Voting_1_ed

Voting_2_sd = dates.Voting_2_sd
Voting_2_ed = dates.Voting_2_ed

Voting_3_sd = dates.Voting_3_sd
Voting_3_ed = dates.Voting_3_ed

Voting_4_sd = dates.Voting_4_sd
Voting_4_ed = dates.Voting_4_ed

result_1_sd = dates.result_1_sd
result_1_ed = dates.result_1_ed

result_2_sd = dates.result_2_sd
result_2_ed = dates.result_2_ed

result_3_sd = dates.result_3_sd
result_3_ed = dates.result_3_ed

result_4_sd = dates.result_4_sd
result_4_ed = dates.result_4_ed

start_con = dates.con_sd
end_con = dates.con_ed


now = timezone.now()

# helper functions

def admincheck(request):
    current_user = request.user
    if current_user.is_authenticated:
        if Admin_user.objects.filter(Userkey=current_user).exists():
            return {'admin': True}
        else:
            return {'admin': False}
    return {'admin': False}

def currentUser_model(request, context):
    if request.user.is_authenticated:
        context['User_Mod'] = User_Model.objects.get(Userkey_id=request.user.id)
    return context


def durationcheck():
    if communityMemberElections_sd <= now <= communityMemberElections_ed:
        std_access.communityMemberElections = True
        std_access.save()   
    else:
        std_access.communityMemberElections = False
        std_access.save()


    if collegeCommunityTrusteeOreHelperElections_sd <= now <= collegeCommunityTrusteeOreHelperElections_ed:
        std_access.collegeCommunityTrusteeOreHelperElections = True
        std_access.save()
    else:
        std_access.collegeCommunityTrusteeOreHelperElections = False
        std_access.save()


    if collegeStudentUnionPresidentOrViceElections_sd <= now <= collegeStudentUnionPresidentOrViceElections_ed:
        std_access.collegeStudentUnionPresidentOrViceElections = True
        std_access.save()
    else:
        std_access.collegeStudentUnionPresidentOrViceElections = False
        std_access.save()

    if universityElections_sd <= now <= universityElections_ed:
        std_access.universityElections = True
        std_access.save()
    else:
        std_access.universityElections = False
        std_access.save()

    if Voting_1_sd <= now <= Voting_1_ed:
        std_access.Voting_1 = True
        std_access.save()
    else:
        std_access.Voting_1 = False
        std_access.save()

    if Voting_2_sd <= now <= Voting_2_ed:
        std_access.Voting_2 = True
        std_access.save()
    else:
        std_access.Voting_2 = False
        std_access.save()

    if Voting_3_sd <= now <= Voting_3_ed:
        std_access.Voting_3 = True
        std_access.save()
    else:
        std_access.Voting_3 = False
        std_access.save()

    if Voting_4_sd <= now <= Voting_4_ed:
        std_access.Voting_4 = True
        std_access.save()
    else:
        std_access.Voting_4 = False
        std_access.save()

    if result_1_sd <= now <= result_1_ed:
        std_access.result_1 = True
        std_access.save()
    else:
        std_access.result_1 = False
        std_access.save()

    if result_2_sd <= now <= result_2_ed:
        std_access.result_2 = True
        std_access.save()
    else:
        std_access.result_2 = False
        std_access.save()

    if result_3_sd <= now <= result_3_ed:
        std_access.result_3 = True
        std_access.save()
    else:
        std_access.result_3 = False
        std_access.save()

    if result_4_sd <= now <= result_4_ed:
        std_access.result_4 = True
        std_access.save()
    else:
        std_access.result_4 = False
        std_access.save()

    return {'std_access': std_access}

@login_required
def loaddata(request, type = 'none'):
        context = admincheck(request)
        loaddataform = loadData(request, request.FILES)
        context['loaddataform'] = loaddataform

        if type == 'original':
            if request.method == 'POST':
                User.objects.filter(is_superuser=False).delete()
                for file in os.listdir('Data/Tables'):
                    read_file_dir = "Data/Tables/"
                    read_rec_dir = 'Data/rec_letters/'
                    read_file = pd.read_excel(read_file_dir + file, sheet_name='Sheet1', skiprows=1)
                    read_file.dropna(inplace=True)
                    read_file = read_file.values.tolist()
                    read_rec_letters = os.listdir(read_rec_dir)
                    for row in read_file:
                        if len(row) == 11 or len(row) == 24:
                            randomNum = ''.join( map( str, [random.choice(range(1, 10)) for _ in range(6) ] ) )
                            user = User.objects.create_user(username=row[0] + randomNum, password='Fcai123456')
                            usermodel = User_Model.objects.create(Userkey = user, Name = row[1], Student_id = row[2], address = row[3], birthdate = row[4], college = row[5], 
                                                                collegeYear = row[6], Voting_status_1 = row[7], 
                                                                Voting_status_2 = row[8], Voting_status_3 = row[9], Voting_status_4 = row[10])
                            rec_letter_exists = False
                            rec = {}
                            for file in read_rec_letters:
                                if file.split('.')[0] == str(row[6]) + "_" + str(row[2]):
                                    rec_letter_exists = True
                                    rec = File(open(read_rec_dir + file, 'rb'))
                            if row[11] and rec_letter_exists:
                                Nominee_user.objects.create(UserModelKey =usermodel, phone_no = row[11], email = row[12], community = row[13], 
                                                            rec_letter = rec, final_list = row[14], role = row[15], 
                                                            communityMemberElections = row[16], collegeCommunityTrusteeOreHelperElections = row[17], 
                                                            collegeStudentUnionPresidentOrViceElections = row[18], universityElections = row[19], 
                                                            communityMemberElectionsNumOfVotes = row[20], 
                                                            collegeCommunityTrusteeOreHelperElectionsNumOfVotes = row[21], 
                                                            collegeStudentUnionPresidentOrViceElectionsNumOfVotes = row[22], 
                                                            universityElectionsNumOfVotes = row[23])
                    context['confirmationmessage'] = 'تم التطبيق بنجاح'

        if type == 'new':
            if request.method == 'POST':
                if loaddataform.is_valid():
                    User.objects.filter(is_superuser=False).delete()
                    read_file = pd.read_excel(loaddataform.cleaned_data['datafile'], sheet_name='Sheet1', skiprows=1)
                    read_file.dropna(inplace=True)
                    read_file = read_file.values.tolist()
                    read_rec_letters = loaddataform.cleaned_data['my_files']
                    for row in read_file:
                        if len(row) == 11 or len(row) == 24:
                            randomNum = ''.join( map( str, [ random.choice(range(1, 10)) for _ in range(6) ] ) )
                            user = User.objects.create_user(username=row[0] + randomNum, password='Fcai123456')
                            usermodel = User_Model.objects.create(Userkey = user, Name = row[1], Student_id = row[2], address = row[3], birthdate = row[4], college = row[5], 
                                                                collegeYear = row[6], Voting_status_1 = row[7], 
                                                                Voting_status_2 = row[8], Voting_status_3 = row[9], Voting_status_4 = row[10])
                            rec_letter_exists = False
                            rec = {}
                            for file in read_rec_letters:
                                if file.name.split('.')[0] == str(row[6]) + "_" + str(row[2]):
                                    rec_letter_exists = True
                                    rec = file
                            if row[11] and rec_letter_exists:
                                Nominee_user.objects.create(UserModelKey =usermodel, phone_no = row[11], email = row[12], community = row[13], 
                                                            rec_letter = rec, final_list = row[14], role = row[15], 
                                                            communityMemberElections = row[16], collegeCommunityTrusteeOreHelperElections = row[17], 
                                                            collegeStudentUnionPresidentOrViceElections = row[18], universityElections = row[19], 
                                                            communityMemberElectionsNumOfVotes = row[20], 
                                                            collegeCommunityTrusteeOreHelperElectionsNumOfVotes = row[21], 
                                                            collegeStudentUnionPresidentOrViceElectionsNumOfVotes = row[22], 
                                                            universityElectionsNumOfVotes = row[23])
                    context['confirmationmessage'] = 'تم الرفع بنجاح'
                else:
                    context['confirmationmessage'] = 'يرجى رفع ملف Excel'


        return context

#Common views

def home(request):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    if context['admin'] == True:
        return redirect('adminp')
    return render(request, 'index.html', context)

def sign_in(request):
    context = admincheck(request)
    currentUser_model(request, context)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_logedin = authenticate(
            request, username=username, password=password)

        if user_logedin is None:
            context.update({"error": "Invalid Username or Password."})
            print("error")
            return render(request, 'login.html', context)

        login(request, user_logedin)

        context = admincheck(request)

        return redirect('home')

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    context = admincheck(request)
    currentUser_model(request, context)
    return redirect('home')

# User related views

@login_required
def nomination(request,type):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)

    if type == 'communityMemberElections':
        if Nominee_user.objects.filter(UserModelKey=User_Mod).exists():
            context.update({"ConfirmationMessage": 'Application already sent'})
            return render(request, 'nomination1.html', context=context)

        else:
            initial_values = {'Name': User_Mod.Name,
                            'nominee_id': User_Mod.Student_id,
                            'address': User_Mod.address,
                            'birthdate': User_Mod.birthdate,
                            'college' : User_Mod.get_college_display,
                            'collegeYear': User_Mod.collegeYear,
                            }
            form = nomForm1(request.POST or None,
                            request.FILES, initial=initial_values)

            if request.POST:
                if form.is_valid():
                    NewNominee = form.save(commit=False)
                    NewNominee.UserModelKey = User_Mod
                    NewNominee.communityMemberElections = True
                    NewNominee.save()
                    context['ConfirmationMessage'] = "Application sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
            context['form'] = form
            return render(request, 'nomination1.html', context=context)
        
    if type == 'collegeCommunityTrusteeOreHelperElections':

        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination2.html', context=context)

        if not (Nominee_user.objects.get(UserModelKey=User_Mod).role == '2'):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination2.html', context=context)

        if Nominee_user.objects.get(UserModelKey=User_Mod).collegeCommunityTrusteeOreHelperElections:
            context.update({"ConfirmationMessage": 'Application already sent'})
            return render(request, 'nomination2.html', context=context)

        else:
            initial_values = {'Name': User_Mod.Name,
                            'nominee_id': User_Mod.Student_id,
                            'address': User_Mod.address,
                            'birthdate': User_Mod.birthdate,
                            'college' : User_Mod.get_college_display,
                            'collegeYear': User_Mod.collegeYear,
                            'phone_no': Nominee_user.objects.get(UserModelKey=User_Mod).phone_no,
                            'email': Nominee_user.objects.get(UserModelKey=User_Mod).email,
                            'community': Nominee_user.objects.get(UserModelKey=User_Mod).get_community_display,
                            'rec_letter': Nominee_user.objects.get(UserModelKey=User_Mod).rec_letter
                            }
            form = nomForm2(request.POST or None,
                            request.FILES, initial=initial_values)

            if request.POST:
                if form.is_valid():
                    NomineeUpdate = Nominee_user.objects.get(UserModelKey=User_Mod)
                    NomineeUpdate.collegeCommunityTrusteeOreHelperElections = True
                    NomineeUpdate.save()
                    context['ConfirmationMessage'] = "Application sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
            context['form'] = form
            return render(request, 'nomination2.html', context=context)
    
    if type == 'collegeStudentUnionPresidentOrViceElections':
        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination3.html', context=context)

        if not ((Nominee_user.objects.get(UserModelKey=User_Mod).role == '3') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '4')):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination3.html', context=context)

        if Nominee_user.objects.get(UserModelKey=User_Mod).collegeStudentUnionPresidentOrViceElections:
            context.update({"ConfirmationMessage": 'Application already sent'})
            return render(request, 'nomination3.html', context=context)

        else:
            initial_values = {'Name': User_Mod.Name,
                            'nominee_id': User_Mod.Student_id,
                            'address': User_Mod.address,
                            'birthdate': User_Mod.birthdate,
                            'college' : User_Mod.get_college_display,
                            'collegeYear': User_Mod.collegeYear,
                            'phone_no': Nominee_user.objects.get(UserModelKey=User_Mod).phone_no,
                            'email': Nominee_user.objects.get(UserModelKey=User_Mod).email,
                            'community': Nominee_user.objects.get(UserModelKey=User_Mod).get_community_display,
                            'rec_letter': Nominee_user.objects.get(UserModelKey=User_Mod).rec_letter
                            }
            form = nomForm3(request.POST or None,
                            request.FILES, initial=initial_values)

            if request.POST:
                if form.is_valid():
                    NomineeUpdate = Nominee_user.objects.get(UserModelKey=User_Mod)
                    NomineeUpdate.collegeStudentUnionPresidentOrViceElections = True
                    NomineeUpdate.save()
                    context['ConfirmationMessage'] = "Application sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
            context['form'] = form
            return render(request, 'nomination3.html', context=context)
            
    if type == 'universityElections':
        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination4.html', context=context)

        if not ((Nominee_user.objects.get(UserModelKey=User_Mod).role == '3') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '4') or
        (Nominee_user.objects.get(UserModelKey=User_Mod).role == '5') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '6')):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination4.html', context=context)

        if Nominee_user.objects.get(UserModelKey=User_Mod).universityElections:
            context.update({"ConfirmationMessage": 'Application already sent'})
            return render(request, 'nomination4.html', context=context)

        else:
            if (Nominee_user.objects.get(UserModelKey=User_Mod).role == '3') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '4'):
                nominateAs = 'أمين/مساعد أمين على مستوى الجامعة'
            else:
                nominateAs = 'رئيس/نائب رئيس الاتحاد للجامعة'

            initial_values = {'Name': User_Mod.Name,
                            'nominee_id': User_Mod.Student_id,
                            'address': User_Mod.address,
                            'birthdate': User_Mod.birthdate,
                            'college' : User_Mod.get_college_display,
                            'collegeYear': User_Mod.collegeYear,
                            'phone_no': Nominee_user.objects.get(UserModelKey=User_Mod).phone_no,
                            'email': Nominee_user.objects.get(UserModelKey=User_Mod).email,
                            'community': Nominee_user.objects.get(UserModelKey=User_Mod).get_community_display,
                            'rec_letter': Nominee_user.objects.get(UserModelKey=User_Mod).rec_letter,
                            'nominateAs': nominateAs
                            }
            form = nomForm4(request.POST or None,
                            request.FILES, initial=initial_values)

            if request.POST:
                if form.is_valid():
                    NomineeUpdate = Nominee_user.objects.get(UserModelKey=User_Mod)
                    NomineeUpdate.universityElections = True
                    NomineeUpdate.save()
                    context['ConfirmationMessage'] = "Application sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
            context['form'] = form
            return render(request, 'nomination4.html', context=context)    



@login_required
def vote(request, type):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)
    if type == 'communityMemberElections':

        if User_Mod.Voting_status_1:
            context.update({"ConfirmationMessage": 'Already voted'})
            return render(request, 'vote1.html', context=context)

        else:
            form = voteForm1(request.POST or None, Userr = User_Mod)
            context.update({
                'form': form
            })
            if request.POST:
                if form.is_valid():
                    User_Mod.Voting_status_1 = 1
                    User_Mod.save()
                    for Community in form.cleaned_data:
                        Nominees = form.cleaned_data[Community]
                        for nom in Nominees:
                            print(nom.communityMemberElectionsNumOfVotes, '\n')
                            nom.communityMemberElectionsNumOfVotes = nom.communityMemberElectionsNumOfVotes + 1
                            Vote.objects.create(nominations_period_id = dates.nominations_period_id,
                                                voter_id=User_Mod, nominee_id=nom.UserModelKey, community = nom.community)
                            
                            print(nom.communityMemberElectionsNumOfVotes, '\n')
                            nom.save()
                    context['ConfirmationMessage'] = "Vote sent successfully"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote1.html', context=context)

    if type == 'collegeCommunityTrusteeOreHelperElections':

        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الانتخاب غير موافاة'})
                return render(request, 'vote2.html', context=context)

        if not (Nominee_user.objects.get(UserModelKey=User_Mod).role == '2'):
                context.update({"ConfirmationMessage": 'متطلبات الانتخاب غير موافاة'})
                return render(request, 'vote2.html', context=context)

        if User_Mod.Voting_status_2:
            context.update({"ConfirmationMessage": 'Already voted'})
            return render(request, 'vote2.html', context=context)

        else:
            UsersinSamecollege = User_Model.objects.filter(college = User_Mod.college)

            if Nominee_user.objects.filter(
        community=Nominee_user.objects.get(UserModelKey=User_Mod).community, UserModelKey__in = UsersinSamecollege, role = '3').exists():
            
                collegeCommunityTrusteeNominee = Nominee_user.objects.get(
            community=Nominee_user.objects.get(UserModelKey=User_Mod).community, UserModelKey__in = UsersinSamecollege, role = '3')
            else:
                collegeCommunityTrusteeNominee = 'الأمين لم يتم تحديده بعد'
            initial_values = {'collegeCommunityTrusteeNominee': collegeCommunityTrusteeNominee,
                }

            form = voteForm2(request.POST or None, Userr = User_Mod, initial = initial_values)
            context.update({
                'form': form
            })
            if request.POST:
                if form.is_valid():
                    User_Mod.Voting_status_2 = 1
                    User_Mod.save()
                    nom = form.cleaned_data['collegeCommunityTrusteeHelperNominee'][0]
                    print (nom)
                    print(nom.collegeCommunityTrusteeOreHelperElectionsNumOfVotes, '\n')
                    nom.collegeCommunityTrusteeOreHelperElectionsNumOfVotes = nom.collegeCommunityTrusteeOreHelperElectionsNumOfVotes + 1
                    Vote.objects.create(nominations_period_id = dates.nominations_period_id,
                                        voter_id=User_Mod, nominee_id=nom.UserModelKey, community = nom.community)
                    
                    print(nom.collegeCommunityTrusteeOreHelperElectionsNumOfVotes, '\n')
                    nom.save()
                    context['ConfirmationMessage'] = "Vote sent successfully"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote2.html', context=context)
    
    if type == 'collegeStudentUnionPresidentOrViceElections':

        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الانتخاب غير موافاة'})
                return render(request, 'vote3.html', context=context)

        if not ((Nominee_user.objects.get(UserModelKey=User_Mod).role == '3') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '4')):
                context.update({"ConfirmationMessage": 'متطلبات الانتخاب غير موافاة'})
                return render(request, 'vote3.html', context=context)

        if User_Mod.Voting_status_3:
            context.update({"ConfirmationMessage": 'Already voted'})
            return render(request, 'vote3.html', context=context)

        else:
            UsersinSamecollege = User_Model.objects.filter(college = User_Mod.college)

            form = voteForm3(request.POST or None, Userr = User_Mod)
            context.update({
                'form': form
            })
            if request.POST:
                if form.is_valid():
                    User_Mod.Voting_status_3 = 1
                    User_Mod.save()
                    nom = form.cleaned_data['collegeStudentUnionPresidentOrVice'][0]
                    print (nom)
                    print(nom.collegeStudentUnionPresidentOrViceElectionsNumOfVotes, '\n')
                    nom.collegeStudentUnionPresidentOrViceElectionsNumOfVotes = nom.collegeStudentUnionPresidentOrViceElectionsNumOfVotes + 1
                    Vote.objects.create(nominations_period_id = dates.nominations_period_id,
                                        voter_id=User_Mod, nominee_id=nom.UserModelKey, community = nom.community)
                    
                    print(nom.collegeStudentUnionPresidentOrViceElectionsNumOfVotes, '\n')
                    nom.save()
                    context['ConfirmationMessage'] = "Vote sent successfully"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote3.html', context=context)
    
    if type == 'universityElections':

        if not (Nominee_user.objects.filter(UserModelKey=User_Mod).exists()):
                context.update({"ConfirmationMessage": 'متطلبات الانتخاب غير موافاة'})
                return render(request, 'vote4.html', context=context)

        if not ((Nominee_user.objects.get(UserModelKey=User_Mod).role == '3') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '4') or
        (Nominee_user.objects.get(UserModelKey=User_Mod).role == '5') or (Nominee_user.objects.get(UserModelKey=User_Mod).role == '6')):
                context.update({"ConfirmationMessage": 'متطلبات الترشح غير موافاة'})
                return render(request, 'nomination4.html', context=context)

        if User_Mod.Voting_status_4:
            context.update({"ConfirmationMessage": 'Already voted'})
            return render(request, 'vote4.html', context=context)

        else:
            form = voteForm4(request.POST or None, Userr = User_Mod)
            context.update({
                'form': form
            })
            if request.POST:
                if form.is_valid():
                    User_Mod.Voting_status_4 = 1
                    User_Mod.save()
                    for Community in form.cleaned_data:
                        Nominees = form.cleaned_data[Community]
                        for nom in Nominees:
                            print(nom.universityElectionsNumOfVotes, '\n')
                            nom.universityElectionsNumOfVotes = nom.universityElectionsNumOfVotes + 1
                            Vote.objects.create(nominations_period_id = dates.nominations_period_id,
                                                voter_id=User_Mod, nominee_id=nom.UserModelKey, community = nom.community)
                            
                            print(nom.universityElectionsNumOfVotes, '\n')
                            nom.save()
                    context['ConfirmationMessage'] = "Vote sent successfully"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote4.html', context=context)    



@login_required
def showresult(request, type):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)

    if type == 'communityMemberElections':

        committee = {}

        for c in Nominee_user.community.field.choices:
            nominees = {}
            i = 1
            UsersinSamecollegeANDcollegeYear = User_Model.objects.filter(college = User_Mod.college, collegeYear = User_Mod.collegeYear)
            NomineesinSamecollegeANDcollegeYear = Nominee_user.objects.filter(UserModelKey__in = UsersinSamecollegeANDcollegeYear, community = c[0], communityMemberElections = True, final_list = True)

            for Nominee in NomineesinSamecollegeANDcollegeYear:
                nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                                'عدد الأصوات': Nominee.communityMemberElectionsNumOfVotes,
                                "الدور": Nominee.get_role_display()}})
                i += 1
                print (Nominee.get_role_display())
            committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})

        context.update({'committee': committee})
        return render(request, 'results1.html', context)
    
    if type == 'collegeCommunityTrusteeOreHelperElections':

        committee = {}

        for c in Nominee_user.community.field.choices:
            nominees = {}
            i = 1
            UsersinSamecollege = User_Model.objects.filter(college = User_Mod.college)
            NomineesinSamecollege = Nominee_user.objects.filter(UserModelKey__in = UsersinSamecollege, community = c[0], collegeCommunityTrusteeOreHelperElections = True, final_list = True)

            for Nominee in NomineesinSamecollege:
                nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                                'عدد الأصوات': Nominee.collegeCommunityTrusteeOreHelperElectionsNumOfVotes,
                                "الدور": Nominee.get_role_display()}})
                i += 1
                print (Nominee)
            committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})

        context.update({'committee': committee})
        return render(request, 'results2.html', context)
    
    if type == 'collegeStudentUnionPresidentOrViceElections':

        committee = {}

        for c in {('1',' ')}:
            nominees = {}
            i = 1
            UsersinSamecollege = User_Model.objects.filter(college = User_Mod.college)
            NomineesinSamecollege = Nominee_user.objects.filter(UserModelKey__in = UsersinSamecollege, collegeStudentUnionPresidentOrViceElections = True, final_list = True)

            for Nominee in NomineesinSamecollege:
                nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                                'عدد الأصوات': Nominee.collegeStudentUnionPresidentOrViceElectionsNumOfVotes,
                                "الدور": Nominee.get_role_display()}})
                i += 1
                print (Nominee.get_role_display())
            committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})

        context.update({'committee': committee})
        return render(request, 'results3.html', context)
        
    if type == 'universityElections':
        
        committee = {}

        for c in Nominee_user.community.field.choices:
            nominees = {}
            i = 1
            for Nominee in Nominee_user.objects.filter(community = c[0], universityElections = True, final_list = True):
                nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                                'عدد الأصوات': Nominee.universityElectionsNumOfVotes,
                                "الدور": Nominee.get_role_display()}})
                i += 1
                print (Nominee.get_role_display())
            committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})
        

        for c in {('8','رئيس الاتحاد/النائب')}:
            nominees = {}
            i = 1
            for Nominee in Nominee_user.objects.filter(community = c[0], universityElections = True, final_list = True):
                nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                                'عدد الأصوات': Nominee.universityElectionsNumOfVotes,
                                "الدور": Nominee.get_role_display()}})
                i += 1
                print (Nominee.get_role_display())
            committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})

        context.update({'committee': committee})
        
        return render(request, 'results4.html', context)


@login_required
def contention(request):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    current_user = request.user
    user_mod = User_Model.objects.get(Userkey_id=current_user.id)


    if Nominee_user.objects.filter(UserModelKey = user_mod):
        initial_values = {'Name': user_mod.Name,
                        'User_id': user_mod.Student_id
                        }
        nom = Nominee_user.objects.get(UserModelKey = user_mod)
        form = ContentionForm(request.POST or None, initial=initial_values ,Userr = user_mod, nom = nom)
        if request.POST:
            if form.is_valid():
                Newcon = form.save(commit=False)
                Newcon.user_id = user_mod
                Newcon.save()
                context['ConfirmationMessage'] = "Application sent successfuly"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"

        context['form'] = form
        return render(request, 'contention.html', context=context)
    
    else:
        context['ConfirmationMessage'] = "contention closed for non nominee"
        return render(request, 'contention.html', context=context)

@login_required
def electoral_program(request):
    context = admincheck(request)
    currentUser_model(request, context)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)

    try:
        nominee_user = Nominee_user.objects.get(UserModelKey=User_Mod)
    except Nominee_user.DoesNotExist:
        return HttpResponseNotFound("You are not a nominee user.")

    if request.method == 'POST':
        form = ElectoralProgForm(request.POST, request.FILES)
        if form.is_valid():
            electoral_prog = form.save(commit=False)
            electoral_prog.nominee_key = nominee_user
            electoral_prog.save()
            return redirect('home')
    else:
        form = ElectoralProgForm()

    return render(request, 'electoral_prog.html', {'form': form})


@login_required
def electoral_prog_show(request):
    current_user = request.user
    user_model = User_Model.objects.get(Userkey_id=current_user.id)
    current_college = user_model.college
    current_college_year = user_model.collegeYear
    programs = electoral_prog.objects.all().filter(nominee_key__UserModelKey__college=current_college,
                                             nominee_key__UserModelKey__collegeYear=current_college_year)
    return render(request, 'electoral_prog_show.html', {'programs': programs})


@login_required
def particular_nominee_prog(request, id):
    electoral_prog_obj = electoral_prog.objects.get(id=id)
    return render(request, 'particular_nominee_prog.html', {'nominee_program': electoral_prog_obj})


# Admin related views

@login_required
def admin(request):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:

        committee = {}
        nominees = {}

        for c in Nominee_user.community.field.choices:
            NumofNominees = Nominee_user.objects.filter(community=c[0]).count()
            committee.update({'c' + c[0]: {'numofNom': NumofNominees}})

        i = 1
        for Nominee in Nominee_user.objects.filter((Q(communityMemberElections = True) | Q(collegeCommunityTrusteeOreHelperElections = True) | Q(collegeStudentUnionPresidentOrViceElections = True) | Q(universityElections = True)) & Q(final_list = True)):
            nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                            'عدد الأصوات': Nominee.communityMemberElectionsNumOfVotes, "اللجنة": Nominee.get_community_display()}})
            i += 1

        context.update({'committee': committee, 'nominees': nominees})
        return render(request, 'adminp1.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')

@login_required
def election_control(request, type):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:
        if type == "new-elections":
            form = Dates_form(request.POST or None)
            context['df'] = form
            if request.method == 'GET':
                try:
                    Nominee_user.objects.all().delete()
                    Contention.objects.all().delete()
                    electoral_prog.all().delete()
                    User_Model.objects.all().update(Voting_status_1 = 0, Voting_status_2 = 0, Voting_status_3 = 0, Voting_status_4 = 0)

                except:
                    {}
                dates.nominations_period_id = dates.nominations_period_id + 1
                dates.save()
                
                context['ConfirmationMessage'] = "تم بداية انتخابات جدبدة"
                return render(request, 'duration.html', context)
        else:
            form = Dates_form(request.POST or None)
            context['df'] = form
            if request.method == 'GET':
                try:
                    Nominee_user.objects.all().update(communityMemberElections = 0,
                        collegeCommunityTrusteeOreHelperElections = 0,
                        collegeStudentUnionPresidentOrViceElections = 0,
                        universityElections = 0,
                        communityMemberElectionsNumOfVotes = 0,           
                        collegeCommunityTrusteeOreHelperElectionsNumOfVotes = 0,                     
                        collegeStudentUnionPresidentOrViceElectionsNumOfVotes = 0,                      
                        universityElectionsNumOfVotes = 0)

                    User_Model.objects.all().update(Voting_status_1 = 0, Voting_status_2 = 0, Voting_status_3 = 0, Voting_status_4 = 0)
                    Contention.objects.all().delete()
                    electoral_prog.all().delete()
                except:
                    {}
                dates.nominations_period_id = dates.nominations_period_id + 1
                dates.save()
                
                context['ConfirmationMessage'] = "تم بداية مرحلة ترشح جديدة"
                return render(request, 'duration.html', context)   
    else:
        return HttpResponse("Invalid request method.")


@login_required
def picksec(request):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:
        current_user = request.user
        user_mod = User_Model.objects.get(Userkey_id=current_user.id)
        form = pickcollegerepres(request.POST or None, Userr = user_mod)
        context.update({
            'form': form
        })
        if request.POST:
            if form.is_valid():
                Nominees = form.cleaned_data
                Nominees[0].role = 'أمين اتحاد'
                Nominees[1].role = 'أمين مساعد اتحاد'
                Nominees[0].save()
                Nominees[1].save()
                context['ConfirmationMessage'] = "تم الحفظ"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"
    return render(request, 'picksec.html', context=context)

@login_required
def duration(request):
    context = admincheck(request)
    currentUser_model(request, context)
    instance = get_object_or_404(Dates, id=1)

    if context['admin'] == True:
        form = Dates_form(request.POST or None, instance = instance)
        context['df'] = form

        if request.POST:
            if form.is_valid():
                form.save()
                context['ConfirmationMessage2'] = "تم التعديل بنجاح"
            else:
                print(form.errors)
        return render(request, 'duration.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')


@login_required
def list_nominee(request, type = 'none'):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:
        context = loaddata(request, type)
        context['nominee'] = Nominee_user.objects.all()
        return render(request, 'listnominee.html',context)
    else:
        return HttpResponse('Erorr 404 Not found')

@login_required
def update_nominee(request, nominee_id):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:

        User_Mod = User_Model.objects.get(Student_id=nominee_id)
        nominee = Nominee_user.objects.get(UserModelKey=User_Mod)
        initial_values = {'Name': nominee.UserModelKey.Name,
                        'nominee_id': nominee.UserModelKey.Student_id,
                        'address': nominee.UserModelKey.address,
                        'birthdate': nominee.UserModelKey.birthdate,
                        'collegeYear': nominee.UserModelKey.collegeYear,
                        }
        form = NomineeForm_update(request.POST or None,
                                instance=nominee, initial=initial_values)

        if request.POST:
            if form.is_valid():
                form.save()
                return redirect(list_nominee)
            else:
                context['ConfirmationMessage'] = "Error: couldn't update nominee"
        context['form'] = form

        return render(request, 'updatenominee.html', context=context)
    else:
        return HttpResponse('Erorr 404 Not found')

@login_required
def result_control(request):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:

        college = ['one','two','three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven'
                ,'Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen',
                'Eighteen','Nineteen','Twenty','Twentyone','Twentytwo','Twentythree','Twentyfour',
                'Twentyfive','Twentysix','Twentyseven','Twentyeight']
        
        for i , item in enumerate(college):
            userinsamecollege = User_Model.objects.filter(college = int(i + 1))
            nominee_list = Nominee_user.objects.filter(final_list = True ,  UserModelKey__in = userinsamecollege)         
            context[item] = nominee_list

        if type == 'communityMemberElections':
            return render(request, 'resultcontrol1.html', context)
        
        if type == 'collegeCommunityTrusteeOreHelperElections':
            return render(request, 'resultcontrol2.html', context)
        
        if type == 'collegeStudentUnionPresidentOrViceElections':
            return render(request, 'resultcontrol3.html', context)
        
        if type == 'universityElections':
            return render(request, 'resultcontrol4.html', context)
        
        return render(request, 'resultcontrol1.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')

@login_required
def update_nominee_result(request, nominee_id):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:
        User_Mod = User_Model.objects.get(Student_id=nominee_id)
        nominee = Nominee_user.objects.get(UserModelKey=User_Mod)
        initial_values = {'Name': nominee.UserModelKey.Name,
                        'nominee_id': nominee.UserModelKey.Student_id,
                        'address': nominee.UserModelKey.address,
                        'birthdate': nominee.UserModelKey.birthdate,
                        'collegeYear': nominee.UserModelKey.collegeYear,
                        }
        form = NomineeForm_update(request.POST or None,
                                instance=nominee, initial=initial_values)

        if request.POST:
            if form.is_valid():
                form.save()
                return redirect(result_control)
            else:
                context['ConfirmationMessage'] = "Error: couldn't update nominee"
        context['form'] = form

        return render(request, 'updatenomineeresult.html', context=context)
    else:
        return HttpResponse('Erorr 404 Not found')
    
@login_required
def list_contention(request):
    context = admincheck(request)
    currentUser_model(request, context)
    if context['admin'] == True:
        contention_list = Contention.objects.all()
        context['nominee'] = contention_list
        return render(request, 'contentioncontrol.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')
