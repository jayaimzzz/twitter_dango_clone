from django.shortcuts import render
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification


def notifications_view(request, user_id):
    html = 'notifications.html'
    user = TwitterUser.objects.filter(user=user_id).first()
    notifications = Notification.objects.filter(user_to_notify=user)
    notifications_copy = map(str,notifications)
    data = {
        'notifications': notifications_copy
    }
    notifications.delete()
    return render(request, html, data)