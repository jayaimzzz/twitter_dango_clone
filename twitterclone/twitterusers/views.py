from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView
from twitterclone.tweets.models import Tweet
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.helpers import get_navbar_data


class NavBarMixIn(object):
    def get_navbar_data(self, request):
        data = {}
        if hasattr(request.user, 'twitteruser'):
            logged_in_user = TwitterUser.objects.filter(user=self.request.user).first()
            qty_of_notifications = Notification.objects.filter(user_to_notify=logged_in_user).count()
            data = {
            'logged_in_user': logged_in_user,
            'qty_of_notifications': qty_of_notifications
            }
        return data


@method_decorator(login_required, name='dispatch')
class IndexView(NavBarMixIn,TemplateView):
    template_name = 'index.html'
   
    def get_context_data(self):
        context = self.get_navbar_data(self.request)
        following = context['logged_in_user'].following.get_queryset()
        tweets = []
        for user in following:
            for tweet in Tweet.objects.filter(author=user):
                tweets.append(tweet)
        context['tweets'] = sorted(tweets, key=lambda tweet: tweet.created, reverse=True) 
        return context


class ProfileView(View):
    def get(self, request, user_name):
        user = TwitterUser.objects.filter(name=user_name).first()
        tweets = Tweet.objects.filter(author=user)
        sorted_tweets = sorted(tweets, key=lambda tweet: tweet.created, reverse=True)
        following = user.following.get_queryset()
        data = {
            'user': user,
            'tweets': sorted_tweets,
            'qty_of_tweets': len(sorted_tweets),
            'follow_unfollow': 'follow',
            'qty_following': following.count()
        }
        if hasattr(request.user, 'twitteruser'):
            data.update(get_navbar_data(request))
            if user in data['logged_in_user'].following.get_queryset():
                data['follow_unfollow'] = 'unfollow'
        html = 'profile.html'
        return render(request, html, data)

@login_required
def toggle_following_view(request, user_name):
    user_to_follow = TwitterUser.objects.filter(name=user_name).first()
    logged_in_user = TwitterUser.objects.filter(user=request.user).first()
    if user_to_follow in logged_in_user.following.get_queryset():
        logged_in_user.following.remove(user_to_follow),
    else:
        logged_in_user.following.add(user_to_follow)
    logged_in_user.save()
    html = 'profile.html'
    return redirect('/profile/' + str(user_name))
