import os
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # do i need api-auth?
    path("api-auth/", include("rest_framework.urls")),
    
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path('terms-of-service/', TemplateView.as_view(template_name="tos.html"), name='terms-of-service'),
    path('privacy-policy/', TemplateView.as_view(template_name="privacy_policy_app.html"), name='privacy'),
    path('support/', TemplateView.as_view(template_name="support.html"), name='support'),
]

if settings.DEBUG==True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Game of Skate Admin Panel"