from allauth.headless.socialaccount import views   
from django.urls import path, include
from .views import LogoutView  # Import the new LogoutView

urlpatterns = [
        # path("_allauth/", include("allauth.headless.urls")),
        # I don't like the headless allauth url structure, renamed here:

        # NOTE: if you ever want to support web and not just the mobil app,
        # copy this line but change 'app' to 'browser' 
        # This is this url but at a different url pattern:
        # https://docs.allauth.org/en/latest/headless/openapi-specification/#tag/Authentication:-Providers/paths/~1_allauth~1%7Bclient%7D~1v1~1auth~1provider~1token/post
        path("provider/token", views.ProviderTokenView.as_api_view(client="app"), name="provider_token"),
        path("logout/", LogoutView.as_view(), name="logout"),  # Delete session token
]