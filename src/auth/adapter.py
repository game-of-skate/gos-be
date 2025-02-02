import json
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import (
    ImproperlyConfigured,
    MultipleObjectsReturned,
)

class AccountAdapter(DefaultAccountAdapter):
    pass
        


# WHY is the client_id alawys none when i go directly to google url?

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        print(f"request.POST {request.POST}")
        print(f"sociallogin\n{type(sociallogin)}\n{sociallogin}")


    # def get_app(self, request, provider, client_id=None):
    #     print("get app AccountSocialAdapter")
    #     from allauth.socialaccount.models import SocialApp
    #     print(f"provider {provider}")
    #     print(f"client_id {client_id}")
    #     print(f"request {request}")
    #     # runs when i go straight to googloe long but not when i use headless properly
    #     # print(request.body)
    #     if not client_id:
    #         print("\n\nwhy no client id? gonna hardcode")
    #         #client_id = "336313820834-ggh95meblen1bagba1ral3v33ahkgu3n.apps.googleusercontent.com"
    #         request_body = dict(request.POST)
    #         client_id = request_body.get("client_id")[0]
    #         print(f"client_id again {client_id}")
    #     apps = self.list_apps(request, provider=provider, client_id=client_id)
    #     print(f"apps {apps}")
    #     if len(apps) > 1:
    #         print("more than one")
    #         visible_apps = [app for app in apps if not app.settings.get("hidden")]
    #         if len(visible_apps) != 1:
    #             raise MultipleObjectsReturned
    #         apps = visible_apps
    #     elif len(apps) == 0:
    #         raise SocialApp.DoesNotExist()
    #     return apps[0]
    

    def get_provider(self, request, provider, client_id=None):
        """Looks up a `provider`, supporting subproviders by looking up by
        `provider_id`.
        """
        from allauth.socialaccount.providers import registry
        print("get provider AccountSocialAdapter")
        print(f"provider {provider}")
        print(f"client_id {client_id}")
        print(f"request {request}")
        # print(request.body)
        if not client_id:
            print("\nno client id in get provider!\n")
            request_body = json.loads(request.body)
            # print(f"request_body {request_body}")
            token = request_body.get("token")
            if token:
                print("token exists!")
                client_id = token.get("client_id")
                print(f"client id {client_id }")

        provider_class = registry.get_class(provider)
        print(f"provider_class {provider_class}")
        if provider_class is None or provider_class.uses_apps:
            app = self.get_app(request, provider=provider, client_id=client_id)
            print(f"app {app}")
            if not provider_class:
                # In this case, the `provider` argument passed was a
                # `provider_id`.
                provider_class = registry.get_class(app.provider)
            if not provider_class:
                raise ImproperlyConfigured(f"unknown provider: {app.provider}")
            print(f"provider class {provider_class}")
            return provider_class(request, app=app)
        elif provider_class:
            assert not provider_class.uses_apps  # nosec
            return provider_class(request, app=None)
        else:
            raise ImproperlyConfigured(f"unknown provider: {app.provider}")
