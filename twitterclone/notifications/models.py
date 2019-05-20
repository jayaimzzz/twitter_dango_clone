from django.db import models
from twitterclone.authentication.models import TwitterUser
from twitterclone.tweets.models import Tweet


class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_to_notify = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user_to_notify} was mentioned in "{self.tweet}"'