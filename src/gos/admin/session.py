from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    readonly_fields = ("user",)

    def user(self, obj):
        decoded = obj.get_decoded()
        return User.objects.get(pk=decoded["_auth_user_id"])  # get the user

    user.short_description = "User"
