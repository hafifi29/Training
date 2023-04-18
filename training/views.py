from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User as User_
from .models import *

# glopal varables
std_acess = Control_content.objects.first()
dates = Dates.objects.first()
start_nomination = datetime.strptime(str(dates.nomin_sd),'%Y-%m-%dT%H:%M')  
end_nomination = datetime.strptime(str(dates.nomin_ed),'%Y-%m-%dT%H:%M')    
start_vote = datetime.strptime(str(dates.vote_sd),'%Y-%m-%dT%H:%M')  
end_vote = datetime.strptime(str(dates.vote_ed),'%Y-%m-%dT%H:%M')    
start_con = datetime.strptime(str(dates.con_sd),'%Y-%m-%dT%H:%M')  
end_con = datetime.strptime(str(dates.con_ed),'%Y-%m-%dT%H:%M')    
# end glopal varables


# Create your views here.


@login_required
def list_nominee(request):
    nominee_list = Nominee_user.objects.all()
    return render(request, 'listnominee.html', {'nominee': nominee_list})


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


def admincheck(request):
    current_user = request.user
    if current_user.is_authenticated:
        if Admin_user.objects.filter(Userkey=current_user).exists():
            return {'admin': True}
        else:
            return {'admin': False}
    return {'admin': False}


def get_data(request):
    if request.method == 'POST':
        dates.nomin_sd = request.POST.get('nomin_start_date')
        dates.nomin_ed = request.POST.get('nomin_end_date')

        dates.vote_sd = request.POST.get('vote_start_date')
        dates.vote_ed = request.POST.get('vote_end_date')

        dates.con_sd = request.POST.get('con_start_date')
        dates.con_ed = request.POST.get('con_end_date')

        dates.save()
    
        std_acess.result = request.POST.get('result')
        std_acess.save()


def dureation():
    print('function colled sucssesfly')
    if start_nomination <= datetime.now() and end_nomination >= datetime.now():
        std_acess.nomination = True
        std_acess.save()
    else:   
        std_acess.nomination = False
        std_acess.save()
    
    # if start_vote <= datetime.now() and end_vote >= datetime.now():
    #     std_acess.vote = True
    #     std_acess.save()
    # else:
    #     std_acess.vote = False
    #     std_acess.save()
        
    # if start_con <= datetime.now() and end_con >= datetime.now():
    #     std_acess.contention = True
    #     std_acess.save()
    # else:
    #     std_acess.contention = False
    #     std_acess.save()



def home(request):
    context = admincheck(request)
    dureation()
    if context['admin'] == True:
        return redirect('adminp')
    return render(request, 'index.html', context)


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
    if start_nomination <= datetime.now() and end_nomination >= datetime.now():
        std_acess.nomination = True
        std_acess.save()
        #End acessabelity code start nomination logic 
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
    else:
        std_acess.nomination = False
        std_acess.save()
        return HttpResponse('Erorr 404 Not found')


@login_required
def vote(request):
    context = admincheck(request)
    #this code for student acessabelity
    if start_vote <= datetime.now() and end_vote >= datetime.now():
        std_acess.vote = True
        std_acess.save()
        #End acessabelity code start nomination logic 
        current_user = request.user
        User_Mod = User_Model.objects.get(Userkey_id=current_user.id)
        if Vote.objects.filter(voter_id=User_Mod).exists():
            context.update({"ConfirmationMessage": 'Already voted'})
            return render(request, 'vote1.html', context=context)

        else:
            form = VoteForm(request.POST or None)
            context.update({
                'form': form
            })
            if request.POST:
                if form.is_valid():
                    for Community in form.cleaned_data:

                        Nominee = form.cleaned_data[Community]
                        Nominee.Numofvotes = Nominee.Numofvotes + 1
                        Vote.objects.create(
                            voter_id=User_Mod, nominee_id=Nominee)
                        print(Nominee.Numofvotes, '\n')
                        Nominee.save()

                        Nominees = form.cleaned_data[Community]
                        for Nominee in Nominees:
                            Nominee.Numofvotes = Nominee.Numofvotes + 1
                            Vote.objects.create(
                                voter_id=User_Mod, nominee_id=Nominee)
                            print(Nominee)
                            Nominee.save()
                    context['ConfirmationMessage'] = "Vote sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote1.html', context=context)
    else:
        if std_acess.vote == True:
            std_acess.vote = False
            std_acess.save()

        return HttpResponse('Erorr 404 Not found')


@login_required
def result(request):
    context = admincheck(request)
    if std_acess.result == True:
        form = ResultForm(request.POST or None)
        context.update({
            'form': form
        })
        context['v'] = "votes"
        if form.is_valid():
            Nominee_id = form.cleaned_data['Nominee_id']
            if User_Model.objects.filter(Student_id=Nominee_id).exists():
                Student = User_Model.objects.get(Student_id=Nominee_id)
                if Nominee_user.objects.filter(UserModelKey=Student).exists():
                    num_of_votes = Nominee_user.objects.get(
                        UserModelKey=Student).Numofvotes
                    context['num_of_votes'] = num_of_votes
            else:
                context['num_of_votes'] = "Nominee not found"
        return render(request, 'results.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')


@login_required
def contention(request):
    context = admincheck(request)
    if start_con <= datetime.now() and end_con >= datetime.now():
        std_acess.contention = True
        std_acess.save()
        #End acessabelity code start nomination logic 
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
    else:
        if std_acess.contention == True:
            std_acess.contention = False
            std_acess.save()
        return HttpResponse('Erorr 404 Not found')


@login_required
def admin(request):
    context = admincheck(request)
    if context['admin'] == True:
        get_data()

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
        print(context)
        return render(request, 'adminp1.html', context,{'df':Dates_form})
    else:
        return HttpResponse('Erorr 404 Not found')
