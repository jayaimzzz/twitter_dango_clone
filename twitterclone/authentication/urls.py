from django.urls import path
from twitterclone.authentication.views import SignUpView, LoginView, LogoutView
# from twitterclone.twitterusers.views import index_view

urlpatterns = [
    # path('', index_view, name='homepage'),
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]