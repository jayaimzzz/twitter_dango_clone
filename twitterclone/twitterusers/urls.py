from django.urls import path
from twitterclone.twitterusers.views import index_view, signup_view

urlpatterns = [
    path('', index_view, name='homepage'),
    path('signup/', signup_view)
]