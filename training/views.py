from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from training.models import User, Nominee, Nominee_user
from django.contrib.auth.models import User as User_

# Create your views here.
# user_object = User.objects.get(user_id = '200130')
# di = {"guest" : user_object.name}


def home(request):

    current_user = request.user

    if current_user is None:
        context = {
            "login": "Login"
        }
    else:
        context = {
            "login": current_user.username
        }

    return render(request, 'index.html', context=context)


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


@login_required
def nomination(request):
    current_user = request.user

    if current_user is None:
        context = {
            "login": "Login"
        }
    else:
        context = {
            "login": current_user.username
        }

    current_user = request.user
    if request.method == "POST":
        id = request.POST.get("name")
        n_id = User_.objects.get(username=id)
        obj = Nominee_user.objects.filter(nominee_id=n_id)

        if n_id is None or not n_id == current_user:
            context = {"error": "Invalid Username"}
            return render(request, 'nom1.html', context=context)
        elif len(obj) != 0:
            context1 = {"error": "you are already nominated"}
            return render(request, 'nom1.html', context=context1)
        phone_no = request.POST.get("phone")
        community = request.POST.get("acdy")
        if community == '1':
            community = 'العلمية'
        elif community == '2':
            community = 'الرياضية'
        elif community == '3':
            community = 'الاجتماعية'
        elif community == '4':
            community = 'أسرةالجوالة'
        elif community == '5':
            community = 'الثقافية'
        elif community == '6':
            community = 'الفنية'
        else:
            community = 'الاسر والرحلات'

        position = "member"
        email = "  "
        final_list = False
        # letter = request.POST.get("comfil")
        Nominee_user.objects.create(nominee_id=n_id, phone_no=phone_no, community=community,
                                    position=position, email=email, final_list=final_list)

    return render(request, 'nom1.html', context=context)


@login_required
def vote(request):
    current_user = request.user

    if current_user is None:
        context = {
            "login": "Login"
        }
    else:
        context = {
            "login": current_user.username
        }

    objs_sport = Nominee_user.objects.filter(community='الرياضية')
    context["Sports"] = objs_sport

    objs_sci = Nominee_user.objects.filter(community='العلمية')
    context["Scientific"] = objs_sci

    objs_soc = Nominee_user.objects.filter(community='الاجتماعية')
    context["Social"] = objs_soc

    objs_scout = Nominee_user.objects.filter(community='أسرةالجوالة')
    context["Scout"] = objs_scout

    objs_cul = Nominee_user.objects.filter(community='الثقافية')
    context["Cultural"] = objs_cul

    objs_art = Nominee_user.objects.filter(community='الفنية')
    context["Art"] = objs_art

    objs_tri = Nominee_user.objects.filter(community='الاسر والرحلات')
    context["Family"] = objs_tri

    if request.method == "POST":
        community = request.POST.get("Scientific committee")

        print("this ia comm", community)

    return render(request, 'vote1.html', context=context)
