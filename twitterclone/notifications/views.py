from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.helpers import get_navbar_data


def notifications_view(request, user_id):
    html = 'notifications.html'
    user = TwitterUser.objects.filter(user=user_id).first()
    notifications = Notification.objects.filter(user_to_notify=user)
    notifications_copy = map(str,notifications)
    notifications.delete()
    data = get_navbar_data(request)
    data['notifications'] = notifications_copy
    return render(request, html, data)