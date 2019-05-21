from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.forms import WriteTweetForm
from twitterclone.tweets.models import Tweet
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.tweets.helpers import make_notifications
from twitterclone.helpers import get_navbar_data


@login_required()
def add_tweet_view(request):
    html = 'addtweet_partial.html'
    form = None
    if request.method == 'POST':
        form = WriteTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = request.user.twitteruser
            tweet = Tweet.objects.create(
                body=data['body'],
                author=author
            )
            make_notifications(tweet)
            return render(request, 'addtweetsuccess.html')
    else:
        form = WriteTweetForm()
    data = get_navbar_data(request)
    data['form'] = form
    return render(request,html, data)

def tweet_view(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first
    data = get_navbar_data(request)
    html = 'tweet.html'
    data['tweet'] = tweet
    return render(request, html, data)
    