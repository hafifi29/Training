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


def nomination(request):
    current_user = request.user

    User_Model = User_Model.objects.get(Name = 'mohamedadel')

    initial_values = {'Name': "UserModel.Name"}
    form = NomineeForm(request.POST or None, initial=initial_values)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        form = NomineeForm()
        context['ConfirmationMessage'] = "Application sent successfuly"
    else:
        context['ConfirmationMessage'] = "Error: couldn't save your application"
        
    return render(request, 'nom1.html', context=context)

def vote(request):
    current_user = request.user
    form = VoteForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        for Nom in form.cleaned_data:
            Nominee_id = form.cleaned_data['Nom']
            if  Nominee_user.objects.filter(nominee_id = Nominee_id).exists():
                num_of_votes = Nominee_user.objects.get(nominee_id = 'Nominee_id').Numofvotes
                num_of_votes = num_of_votes + 1
                form = VoteForm()
                context['ConfirmationMessage'] = "Vote sent successfuly"
            else:
                context['ConfirmationMessage'] = "Nominee not found"
    return render(request, 'vote1.html', context=context)

def result(request):

    form = ResultForm(request.POST or None)
    context = {
        'form': form     
    }
    if form.is_valid():
            Nominee_id = form.cleaned_data['Nominee_id']
            if  Nominee_user.objects.filter(nominee_id = Nominee_id).exists():
                num_of_votes = Nominee_user.objects.get(nominee_id = Nominee_id).Numofvotes
                form = ResultForm()
                context['num_of_votes'] = num_of_votes
            else:
                context['num_of_votes'] = "Nominee not found"
    return render(request,'results.html',context)