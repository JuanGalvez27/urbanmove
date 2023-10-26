from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from urbanmove.authentication import BearerAuthentication


class CustomObtainAuthToken(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serialializer = AuthTokenSerializer(data=request.data)
        if serialializer.is_valid():
            user = serialializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serialializer.errors, status=status.HTTP_400_BAD_REQUEST)
