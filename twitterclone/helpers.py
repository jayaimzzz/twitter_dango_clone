# from twitterclone.authentication.models import TwitterUser
# from twitterclone.notifications.models import Notification

# def get_navbar_data(request):
#     data = {}
#     if hasattr(request.user, 'twitteruser'):
#         logged_in_user = TwitterUser.objects.filter(user=request.user).first()
#         qty_of_notifications = Notification.objects.filter(user_to_notify=logged_in_user).count()
#         data = {
#         'logged_in_user': logged_in_user,
#         'qty_of_notifications': qty_of_notifications
#         }
#     return data