from django.urls import path
from twitterclone.twitterusers.views import IndexView, ProfileView, ToggleFollowingView

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('profile/<str:user_name>/', ProfileView.as_view(), name='profile'),
    path('profile/', IndexView.as_view()),
    # path('follow/<str:user_name>/', toggle_following_view)
    path('follow/<str:user_name>/', ToggleFollowingView.as_view())
]