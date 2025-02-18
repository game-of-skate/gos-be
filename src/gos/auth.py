from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class SessionTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        session_token = request.META.get("HTTP_X_SESSION_TOKEN")
        # Could also get specifically from the request.headers
        # session_token = request.headers.get('X-Session-Token')
        if not session_token:
            return None  # authentication did not succeed
        try:
            s = Session.objects.get(session_key=session_token)
            decoded = s.get_decoded()
            user = User.objects.get(pk=decoded["_auth_user_id"])  # get the user
        except (Session.DoesNotExist, User.DoesNotExist):
            raise exceptions.AuthenticationFailed(
                "No such user"
            )  # raise exception if user does not exist

        return (user, None)  # authentication successful
