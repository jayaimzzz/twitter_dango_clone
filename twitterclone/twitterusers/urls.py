from django.urls import path
from twitterclone.twitterusers.views import index_view, profile_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('profile/<int:user_id>/', profile_view),
    path('follow/<int:user_id>/', follow_success_view)
]