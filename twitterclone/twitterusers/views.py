from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.models import Tweet


@login_required()
def index_view(request):
    tweets = Tweet.objects.all()
    sorted_tweets = sorted(tweets,key=lambda tweet: tweet.created, reverse=True)
    html = 'index.html'
    return render(request,html, {'tweets': sorted_tweets})
