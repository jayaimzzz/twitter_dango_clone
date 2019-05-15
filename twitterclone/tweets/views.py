from django.shortcuts import render
from twitterclone.tweets.forms import WriteTweetForm
from twitterclone.tweets.models import Tweet

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