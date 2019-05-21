from django.urls import path
from twitterclone.notifications.views import notifications_view
from twitterclone.twitterusers.views import index_view

urlpatterns = [
    path('notifications/<int:user_id>', notifications_view),
    path('notifications/', index_view)
]