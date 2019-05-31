from django.urls import path
from twitterclone.notifications.views import NotificationsView
from twitterclone.twitterusers.views import IndexView

urlpatterns = [
    path('notifications/<int:user_id>', NotificationsView.as_view()),
    path('notifications/', IndexView.as_view())
]