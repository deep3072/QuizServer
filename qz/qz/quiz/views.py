# Create your views here.

from django.shortcuts import render
from quiz.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from .models import Question
from .models import Course

mydict = {}


def index(request):
    return render(request, "quiz/index.html")


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'quiz/registration.html',
                          {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'quiz/login.html', {})


def contact(request):
    return HttpResponse("<h1>Contact Us page </h1>")


@login_required
def quiz_world(request):
    courses = Course.objects.all()
    questions = Question.objects.all()
    user = str(request.user.username)
    if "request.session['seen_status']" != False:
        request.session['seen_status'] = False
        for i in range(1, 100):
            mydict[i, user] = True
    params = {'quiz_name': courses, 'question': questions}
    return render(request, 'quiz/quiz_world.html', params)


@login_required
def quizview(request, course_name):
    courses = Course.objects.all()
    questions = Question.objects.all()
    user = str(request.user.username)
    params = {'quiz_name': courses, 'question': questions, 'current_quiz': course_name}
    for i in courses:
        if i.course_name == course_name and mydict[i.id, user] == True:
            mydict[i.id, user] = False
            return render(request, 'quiz/quiz_view.html', params)
    return render(request, 'quiz/quiz_attemped.html', params)
