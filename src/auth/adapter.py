import json
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    pass


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def get_provider(self, request, provider, client_id=None):
        """
        Subclassed so that having > 1 client per provider doesn't silently break everything
        I don't even know if I'll do this, but this was super super confusing to debug
        So leaving a a reminder.
        The reason is, no client_id is provided when SocialAccount.get_provider,
        which happens when new account is created.
        """
        if not client_id:
            # check request body for provider, which will be there if this was initiated from
            # a call to _allauth/app/v1/auth/provider/token
            request_body = json.loads(request.body)
            token = request_body.get("token")
            if token:
                client_id = token.get("client_id")

        return super().get_provider(
            request=request, provider=provider, client_id=client_id
        )
