from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from twitterclone.authentication.models import TwitterUser
from twitterclone.authentication.forms import SignupForm, LoginForm


def signup_view(request):
    html = 'generic_form.html'
    form = None

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['username'], data['password']
            )
            login(request, user)
            TwitterUser.objects.create(
                name=data['username'],
                user=user
            )
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return(request, '<h1>form not valid</h1>')
    else:
        form = SignupForm()
    return render(request, html, {'form':form, 'title': 'signup'})


def login_view(request):
    html='generic_form.html'
    form = None
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next','/'))
    else:
        form = LoginForm()
    return render(request, html, {'form':form, 'title': 'login'})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))