from django.urls import path
from twitterclone.notifications.views import notifications_view
from twitterclone.twitterusers.views import IndexView

urlpatterns = [
    path('notifications/<int:user_id>', notifications_view),
    path('notifications/', IndexView.as_view())
]