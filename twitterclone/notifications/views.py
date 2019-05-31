from django.views.generic import TemplateView
from twitterclone.authentication.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.twitterusers.views import NavBarMixIn


class NotificationsView(NavBarMixIn,TemplateView):
    template_name = 'notifications.html'

    def get_context_data(self,user_id):
        user = TwitterUser.objects.filter(user=user_id).first()
        notifications = Notification.objects.filter(user_to_notify=user)
        notifications_copy = map(str,notifications)
        notifications.delete()
        context = self.get_navbar_data(self.request)
        context['notifications'] = notifications_copy
        return context
