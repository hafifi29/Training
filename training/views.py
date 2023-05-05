from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User as User_
from .models import *
from datetime import datetime
from django.utils import timezone


# global varables
std_access = Control_content.objects.first()
dates = Dates.objects.first()
start_nomination = dates.nomin_sd
end_nomination = dates.nomin_ed
start_vote = dates.vote_sd
end_vote = dates.vote_ed
start_con = dates.con_sd
end_con = dates.con_ed
now = timezone.now()
# end global varables

# Create your views here.

# helper functions


def admincheck(request):
    current_user = request.user
    if current_user.is_authenticated:
        if Admin_user.objects.filter(Userkey=current_user).exists():
            return {'admin': True}
        else:
            return {'admin': False}
    return {'admin': False}


def durationcheck():
    if start_nomination <= now <= end_nomination:
        std_access.nomination = True
        std_access.save()
    else:
        std_access.nomination = False
        std_access.save()

    if start_vote <= now <= end_vote:
        std_access.vote = True
        std_access.save()
    else:
        std_access.vote = False
        std_access.save()

    if start_con <= now <= end_con:
        std_access.contention = True
        std_access.save()
    else:
        std_access.contention = False
        std_access.save()
    return {'std_access': std_access}


def home(request):
    context = admincheck(request)
    durationcheck()
    if context['admin'] == True:
        return redirect('adminp')
    return render(request, 'index.html', context)


# User related views

def sign_in(request):

    context = admincheck(request)

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
    return redirect('home')


@login_required
def nomination(request):
    context = admincheck(request)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)
    if Nominee_user.objects.filter(UserModelKey=User_Mod).exists():
        context.update({"ConfirmationMessage": 'Application already sent'})
        return render(request, 'nom1.html', context=context)

    else:
        initial_values = {'Name': User_Mod.Name,
                          'nominee_id': User_Mod.Student_id,
                          'address': User_Mod.address,
                          'birthdate': User_Mod.birthdate,
                          'collegeYear': User_Mod.collegeYear,
                          }
        form = NomineeForm(request.POST or None,
                           request.FILES, initial=initial_values)

        if request.POST:
            if form.is_valid():
                NewNominee = form.save(commit=False)
                NewNominee.UserModelKey = User_Mod
                NewNominee.save()
                context['ConfirmationMessage'] = "Application sent successfuly"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"
        context['form'] = form
        return render(request, 'nom1.html', context=context)


@login_required
def vote(request):
    context = admincheck(request)
    context.update(durationcheck())
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)
    if User_Mod.Voting_status:
        context.update({"ConfirmationMessage": 'Already voted'})
        return render(request, 'vote1.html', context=context)

    else:
        form = VoteForm(request.POST or None)
        context.update({
            'form': form
        })
        if request.POST:
            if form.is_valid():
                User_Mod.Voting_status = 1
                User_Mod.save()
                for Community in form.cleaned_data:
                    Nominees = form.cleaned_data[Community]
                    for nom in Nominees:
                        print(nom.Numofvotes, '\n')
                        nom.Numofvotes = nom.Numofvotes + 1
                        Vote.objects.create(nominations_period_id = dates.nominations_period_id,
                                             voter_id=User_Mod, nominee_id=nom.UserModelKey, community = nom.community)
                        
                        print(nom.Numofvotes, '\n')
                        nom.save()
                context['ConfirmationMessage'] = "Vote sent successfully"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"
    return render(request, 'vote1.html', context=context)


@login_required
def result(request):
    context = admincheck(request)
    context.update(durationcheck())

    committee = {}

    for c in Nominee_user.community.field.choices:
        nominees = {}
        i = 1
        for Nominee in Nominee_user.objects.filter(community = c[0]):
            nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                            'عدد الأصوات': Nominee.Numofvotes}})
            i += 1

        committee.update({'c' + c[0] : {'name': c[1],'nominees': nominees}})

    context.update({'committee': committee})
    print (context)
    return render(request, 'results.html', context)


@login_required
def contention(request):
    context = admincheck(request)
    context.update(durationcheck())
    current_user = request.user
    user_mod = User_Model.objects.get(Userkey_id=current_user.id)
    initial_values = {'Name': user_mod.Name,
                      'User_id': user_mod.Student_id
                      }
    form = ContentionForm(request.POST or None, initial=initial_values)
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


# Admin related views

@login_required
def admin(request):
    context = admincheck(request)
    if context['admin'] == True:

        committee = {}
        nominees = {}

        for c in Nominee_user.community.field.choices:
            NumofNominees = Nominee_user.objects.filter(community=c[0]).count()
            committee.update({'c' + c[0]: {'numofNom': NumofNominees}})

        i = 1
        for Nominee in Nominee_user.objects.all():
            nominees.update({'n'+str(i): {'الاسم': Nominee.UserModelKey.Name,
                            'عدد الأصوات': Nominee.Numofvotes, "اللجنة": Nominee.get_community_display()}})
            i += 1

        context.update({'committee': committee, 'nominees': nominees})
        return render(request, 'adminp1.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')

@login_required
def new_elections(request):
    context = admincheck(request)
    if context['admin'] == True:
        form = Dates_form(request.POST or None)
        context['df'] = form
        if request.method == 'GET':
            Nominee_user.objects.all().delete()
            Contention.objects.all().delete()
            User_Model.objects.update(Voting_status = 0)
            dates.nominations_period_id = dates.nominations_period_id + 1
            dates.save()
            
            context['ConfirmationMessage'] = "تم بداية مرحلة ترشح جديدة"
            return render(request, 'duration.html', context)
        else:
            return HttpResponse("Invalid request method.")
        
@login_required
def duration(request):
    context = admincheck(request)
    if context['admin'] == True:
        form = Dates_form(request.POST or None)
        context['df'] = form

        if request.POST:
            if form.is_valid():
                save_data(request, form)
                context['ConfirmationMessage'] = "تم التعديل بنجاح"
            else:
                print(form.errors)
        return render(request, 'duration.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')


@login_required
def list_nominee(request):
    nominee_list = Nominee_user.objects.all()
    return render(request, 'listnominee.html', {'nominee': nominee_list})


@login_required
def list_contention(request):
    contention_list = Contention.objects.all()
    print(contention_list)
    return render(request, 'contentioncontrol.html', {'nominee': contention_list})


@login_required
def update_nominee(request, nominee_id):
    context = {}
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


def save_data(request, form):
    if form.is_valid():
        dates.nomin_sd = form.cleaned_data['nomin_start_date']
        dates.nomin_ed = form.cleaned_data['nomin_end_date']

        dates.vote_sd = form.cleaned_data['vote_start_date']
        dates.vote_ed = form.cleaned_data['vote_end_date']

        dates.con_sd = form.cleaned_data['con_start_date']
        dates.con_ed = form.cleaned_data['con_end_date']

        dates.save()

        std_access.result = form.cleaned_data['result']
        std_access.save()
