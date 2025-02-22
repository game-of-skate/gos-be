from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sessions.models import Session

from rest_framework.permissions import IsAuthenticated

from ..auth import SessionTokenAuthentication


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionTokenAuthentication,)

    def post(self, request):
        session_token = request.META.get("HTTP_X_SESSION_TOKEN")
        if not session_token:
            return Response(
                {"detail": "Session token not provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            session = Session.objects.get(session_key=session_token)
            session.delete()  # Delete the session
            return Response(
                {"detail": "Logged out successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Session.DoesNotExist:
            return Response(
                {"detail": "Session does not exist."}, status=status.HTTP_404_NOT_FOUND
            )
