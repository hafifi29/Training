from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from training.models import Nominee_user
from .forms import NomineeForm, VoteForm
from django.contrib.auth.models import User as User_

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


def nomination(request):

    current_user = request.user
    form = NomineeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NomineeForm()
    context = {
        'form': form
        }
    return render(request, 'nom1.html', context=context)


def vote(request):

    current_user = request.user
    form = VoteForm(request.POST or None)
    if form.is_valid():
        for item in form.cleaned_data:
            Nominee = Nominee.objects.get(id=item)
        #    Nominee.numofvotes +1
            form = VoteForm()
    context = {
        'form': form
        }
    return render(request, 'vote1.html', context=context)
