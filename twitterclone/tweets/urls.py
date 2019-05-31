from django.urls import path
from twitterclone.tweets.views import AddTweetView, TweetView

urlpatterns = [
    path('addtweet/', AddTweetView.as_view()),
    path('tweet/<int:tweet_id>/', TweetView.as_view())
]