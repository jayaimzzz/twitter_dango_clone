from django.shortcuts import render, redirect
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
    tweets = Tweet.objects.filter(author=user)
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.created, reverse=True)
    data = {
        'user': user,
        'tweets': sorted_tweets,
        'qty_of_tweets': len(sorted_tweets),
        'follow_unfollow': 'follow'
    }
    if hasattr(request.user, 'twitteruser'):
        logged_in_user = TwitterUser.objects.filter(user=request.user).first()
        if user in logged_in_user.following.get_queryset():
            data['follow_unfollow'] = 'unfollow'
    html = 'profile.html'
    return render(request, html, data)

@login_required
def toggle_following_view(request, user_id):
    user_to_follow = TwitterUser.objects.filter(user=user_id).first()
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    if user_to_follow in logged_in_user.following.get_queryset():
        logged_in_user.following.remove(user_to_follow),
    else:
        logged_in_user.following.add(user_to_follow)
    logged_in_user.save()
    html = 'profile.html'
    return redirect('/profile/' + str(user_id))
