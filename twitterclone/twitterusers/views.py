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
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    tweets = Tweet.objects.filter(author=user)
    sorted_tweets = sorted(tweets, key=lambda tweet: tweet.created, reverse=True)
    html = 'profile.html'
    # print(dir(logged_in_user.following))
    if user in logged_in_user.following.get_queryset():
        follow_unfollow = 'unfollow'
    else:
        follow_unfollow = 'follow'
    return render(request, html, {
        'user': user, 
        'tweets': sorted_tweets,
        'follow_unfollow': follow_unfollow
        })


def toggle_following_view(request, user_id):
    user_to_follow = TwitterUser.objects.filter(user=user_id).first()
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    if user_to_follow in logged_in_user.following.get_queryset():
        logged_in_user.following.remove(user_to_follow),
    else:
        logged_in_user.following.add(user_to_follow)
    logged_in_user.save()
    html = 'profile.html'
    # return profile_view(request, user_id)
    return redirect('/profile/' + str(user_id))
