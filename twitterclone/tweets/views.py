from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from twitterclone.tweets.forms import WriteTweetForm
from twitterclone.tweets.models import Tweet
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.authentication.models import TwitterUser
from twitterclone.twitterusers.views import NavBarMixIn


class MakeNotificationMixIn(object):
    def make_notifications(self, tweet):
        tweet_list = str(tweet).split()
        twitter_users = TwitterUser.objects.all()
        mentions = [word[1:] for word in tweet_list if word.startswith('@')]
        for mention in mentions:
            for user in twitter_users:
                if mention.lower() == user.name.lower():
                    Notification.objects.create(
                        tweet=tweet,
                        user_to_notify=user
                    )


@method_decorator(login_required, name='dispatch')
class AddTweetView(MakeNotificationMixIn, FormView):
    template_name = 'addtweet_partial.html'
    form_class = WriteTweetForm
    success_url = 'addtweetsuccess.html'

    def form_valid(self, form):
        data = form.cleaned_data
        author = self.request.user.twitteruser
        tweet = Tweet.objects.create(
            body=data['body'],
            author=author
        )
        self.make_notifications(tweet)
        return render(self.request, self.success_url)
    

class TweetView(NavBarMixIn,TemplateView):
    template_name = 'tweet.html'
    
    def get_context_data(self, tweet_id):
        context = self.get_navbar_data(self.request)
        context['tweet'] = Tweet.objects.filter(id=tweet_id).first()
        return context
        