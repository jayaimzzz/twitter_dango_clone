from django.urls import path
from twitterclone.twitterusers.views import index_view, profile_view, toggle_following_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('follow/<int:user_id>/', toggle_following_view)
]