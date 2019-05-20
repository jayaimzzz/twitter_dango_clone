from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.forms import WriteTweetForm
from twitterclone.tweets.models import Tweet

@login_required()
def add_tweet_view(request):
    html = 'addtweet_partial.html'
    form = None
    if request.method == 'POST':
        form = WriteTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            author = request.user.twitteruser
            Tweet.objects.create(
                body=data['body'],
                author=author
            )
            return render(request, 'addtweetsuccess.html')
    else:
        form = WriteTweetForm()
    return render(request,html, {'form':form})

def tweet_view(request, tweet_id):

    tweet = Tweet.objects.filter(id=tweet_id).first
    html = 'tweet.html'
    return render(request, html, {'tweet':tweet})
    