from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NomineeForm, VoteForm, ResultForm, ContentionForm
from django.contrib.auth.models import User as User_
from .models import Vote, Nominee_user, Contention, Admin_user
from .models import User_Model
from .models import Control_content

# Create your views here.


def admincheck(request):
    current_user = request.user
    if current_user.is_authenticated:
        if Admin_user.objects.filter(Userkey=current_user).exists():
            return {'admin': True}
        else:
            return {'admin': False}
    return {'admin': False}


def home(request):
    context = admincheck(request)
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

        if context['admin'] == True:
            return render(request, 'adminp1.html', context)

        return redirect('home')
    
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    context = admincheck(request)
    return render(request, 'index.html',context)

@login_required
def nomination(request):
    context = admincheck(request)
    if Control_content.objects.first().nomination == True:

        current_user = request.user
        User_Mod = User_Model.objects.get(Userkey_id = current_user.id)
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
            form = NomineeForm(request.POST or None, request.FILES, initial=initial_values)

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
        return HttpResponse('Erorr 404 Not found')


@login_required
def vote(request):
    context = admincheck(request)
    if Control_content.objects.first().vote == True:

        current_user = request.user
        User_Mod = User_Model.objects.get(Userkey_id = current_user.id)
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
                        Nominees = form.cleaned_data[Community]
                        for Nominee in Nominees:
                            Nominee.Numofvotes = Nominee.Numofvotes + 1
                            Vote.objects.create(voter_id = User_Mod, nominee_id = Nominee)
                            print (Nominee)
                            Nominee.save()
                    context['ConfirmationMessage'] = "Vote sent successfuly"
                else:
                    context['ConfirmationMessage'] = "Error: couldn't save application"
        return render(request, 'vote1.html', context=context)
    else:
        return HttpResponse('Erorr 404 Not found')



@login_required
def result(request):
    context = admincheck(request)
    if Control_content.objects.first().result == True:
        form = ResultForm(request.POST or None)
        context.update({
            'form': form
        })
        context['v'] = "votes"
        if form.is_valid():
                Nominee_id = form.cleaned_data['Nominee_id']
                if User_Model.objects.filter(Student_id = Nominee_id).exists():
                    Student = User_Model.objects.get(Student_id = Nominee_id)
                    if  Nominee_user.objects.filter(UserModelKey = Student).exists():
                        num_of_votes = Nominee_user.objects.get(UserModelKey = Student).Numofvotes
                        context['num_of_votes'] = num_of_votes
                else:
                    context['num_of_votes'] = "Nominee not found"
        return render(request,'results.html',context)
    else:
        return HttpResponse('Erorr 404 Not found')
    

@login_required
def contention(request):
    context = admincheck(request)
    if Control_content.objects.first().result == True:
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
        return HttpResponse('Erorr 404 Not found')

@login_required
def admin(request):
    context = admincheck(request)
    if context['admin'] == True:
        for c in Nominee_user.community.field.choices:
            NumofNom = Nominee_user.objects.filter(community = c[0]).count()
            context.update({c[0]: NumofNom})
        print(context)
        return render(request, 'adminp1.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')
