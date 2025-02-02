import os
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from allauth.headless.constants import Client
from auth.views import login_by_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "terms-of-service/",
        TemplateView.as_view(template_name="tos.html"),
        name="terms-of-service",
    ),
    path(
        "privacy-policy/",
        TemplateView.as_view(template_name="privacy_policy_app.html"),
        name="privacy",
    ),
    path(
        "support/", TemplateView.as_view(template_name="support.html"), name="support"
    ),
    path("accounts/", include("allauth.urls")),
    # Include the API endpoints:
    path("_allauth/", include("allauth.headless.urls")),
    # api-auth only if intend to use the browsable API
    # path("api-auth/", include("rest_framework.urls")),
    path(
        "auth/social/login/google",
        login_by_token,
        name="google-login",
    ),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Game of Skate Admin Panel"
