from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NomineeForm, VoteForm, ResultForm
from django.contrib.auth.models import User as User_
from .models import Vote, Nominee_user
from .models import User_Model

# Create your views here.
# user_object = User.objects.get(user_id = '200130')
# di = {"guest" : user_object.name}

def home(request):
    current_user = request.user
    return render(request, 'index.html')

def sign_in(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_logedin = authenticate(
            request, username=username, password=password)

        if user_logedin is None:
            context = {"error": "Invalid Username or Password."}
            print("error")
            return render(request, 'login.html', context=context)

        login(request, user_logedin)
        return redirect('home')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def nomination(request):
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id = current_user.id)
    if Nominee_user.objects.filter(UserModelKey=User_Mod).exists():
        context = {"ConfirmationMessage": 'Application already sent'}
        return render(request, 'nom1.html', context=context)
    
    else:
        initial_values = {'Name': User_Mod.Name,
                        'nominee_id': User_Mod.Student_id,
                        'address': User_Mod.address,
                            'birthdate': User_Mod.birthdate,
                            'collegeYear': User_Mod.collegeYear,
                        }
        form = NomineeForm(request.POST or None, request.FILES, initial=initial_values)
        context = {} 
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
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id = current_user.id)
    if Vote.objects.filter(voter_id=User_Mod).exists():
        context = {"ConfirmationMessage": 'Already voted'}
        return render(request, 'vote1.html', context=context)

    else:
        form = VoteForm(request.POST or None)
        context = {
            'form': form
        }
        if request.POST:
            if form.is_valid():
                for Community in form.cleaned_data:
                    Nominee = form.cleaned_data[Community]
                    Nominee.Numofvotes = Nominee.Numofvotes + 1
                    Vote.objects.create(voter_id = User_Mod, nominee_id = Nominee)
                    print (Nominee.Numofvotes, '\n')
                    Nominee.save()
                context['ConfirmationMessage'] = "Vote sent successfuly"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"
    return render(request, 'vote1.html', context=context)


@login_required
def result(request):

    form = ResultForm(request.POST or None)
    context = {
        'form': form     
    }
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