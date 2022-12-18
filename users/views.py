from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.conf import settings
from users.utils import send_mass_html_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import (
    PasswordResetSerializer,
    PasswordSerializer,
    PasswordChangeSerializer,
)


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        user = User.objects.get(email=request.data["email"])
        uid = data["uid"]
        token = data["token"]
        url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}"
        html_content = render_to_string(
            "emails/password_reset.html", {"user": user, "url": url}
        )
        text_content = striptags(html_content)
        data_tuples = []
        data_tuples.append(
            [
                "Restablecer contraseña",
                text_content,
                html_content,
                settings.EMAIL_FROM,
                [user.email],
            ]
        )
        send_mass_html_mail(data_tuples)
        return Response(serializer.data)


class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        pk = urlsafe_base64_decode(uidb64).decode("utf-8")
        user = User.objects.get(id=pk)
        if default_token_generator.check_token(user, token):
            serializer = PasswordSerializer(
                data=request.data,
                context={"request": request},
            )
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({"status": "success"})
        return Response({"status": "fail"})


@api_view(["post"])
@permission_classes((permissions.IsAuthenticated,))
def change_password(request):
    serializer = PasswordChangeSerializer(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"status": "Success."})
