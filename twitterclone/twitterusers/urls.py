from django.urls import path
from twitterclone.twitterusers.views import index_view, profile_view, toggle_following_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('profile/<str:user_name>/', profile_view, name='profile'),
    path('profile/', index_view),
    path('follow/<str:user_name>/', toggle_following_view)
]