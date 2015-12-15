from .models import User
import datetime
from django.contrib import messages
import arrow


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        """
        Get an instance of User using the supplied email and check its password
        """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                if arrow.get(user.subscription_end) >= arrow.now():
                    return user
                else:
                    return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Used by the django authentication system to retrieve an instance of User
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
