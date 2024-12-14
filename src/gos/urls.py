from django.contrib import admin
from django.urls import include, path
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
]
