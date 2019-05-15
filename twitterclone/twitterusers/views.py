from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.models import Tweet


@login_required()
def index_view(request):
    tweets = Tweet.objects.all()
    html = 'index.html'
    return render(request,html)
