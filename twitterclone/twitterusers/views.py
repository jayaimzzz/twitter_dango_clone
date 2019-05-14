from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.twitterusers.forms import SignupForm

def index_view(request):
    html = 'index.html'
    return render(request,html)

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