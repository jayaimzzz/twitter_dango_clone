# navbar needs
# logged_in_user
# qty_of_notifications

from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification

def get_navbar_info(request):
    logged_in_user = TwitterUser.objects.filter(user=request.user)first()
    pass
