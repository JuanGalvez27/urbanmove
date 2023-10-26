from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from urbanmove.core.models import City
from urbanmove.permissions import IsOperator

from .serializers import CitySerializer
from urbanmove.authentication import BearerAuthentication


class CityModelViewSet(viewsets.ModelViewSet):
    """
    Viewset that provides the standard actions for city
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsOperator]
    serializer_class = CitySerializer
    queryset = City.objects.all()
    http_method_names = ["get", "post", "delete", "put"]
