from django.urls import path
from twitterclone.twitterusers.views import index_view

urlpatterns = [
    path('', index_view, name='homepage'),
]