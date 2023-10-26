from django.contrib.auth import authenticate, get_user_model, login
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from urbanmove.users.api.serializers import  UserSerializer
from rest_framework.views import APIView




User = get_user_model()

class UserAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

