from allauth.socialaccount.providers.google.views import LoginByTokenView
from allauth.socialaccount.helpers import (
    complete_social_login,
    render_authentication_error,
)
from django.views.decorators.csrf import csrf_exempt

class GoogleTokenView(LoginByTokenView):
    def post(self, request, *args, **kwargs):
        credential = request.POST.get("credential")
        login = self.provider.verify_token(request, {"id_token": credential})
        return complete_social_login(request, login)
login_by_token = csrf_exempt(GoogleTokenView.as_view())