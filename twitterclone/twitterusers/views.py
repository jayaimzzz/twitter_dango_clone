from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.models import Tweet
from twitterclone.authentication.models import TwitterUser



@login_required()
def index_view(request):
    tweets = Tweet.objects.all()
    sorted_tweets = sorted(tweets,key=lambda tweet: tweet.created, reverse=True)
    html = 'index.html'
    return render(request, html, {'tweets': sorted_tweets})

def profile_view(request, user_id):
    user = TwitterUser.objects.filter(user=user_id).first()
    # user = TwitterUser.objects.get(user=user_id)
    tweets = Tweet.objects.filter(author=user)
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.created, reverse=True)
    html = 'profile.html'
    return render(request, html, {
        'user': user, 
        'tweets': sorted_tweets
        })

def follow_success_view(request, user_id):
    