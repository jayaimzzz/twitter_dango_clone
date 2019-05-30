from django.urls import path
from twitterclone.authentication.views import signup_view, login_view, logout_view
# from twitterclone.twitterusers.views import index_view

urlpatterns = [
    # path('', index_view, name='homepage'),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view)
]