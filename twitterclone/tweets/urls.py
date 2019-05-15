from django.urls import path
from twitterclone.tweets.views import add_tweet_view

urlpatterns = [
    path('addtweet/', add_tweet_view)
]