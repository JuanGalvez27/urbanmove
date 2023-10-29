from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from urbanmove.core.models import City, BusStop, BusRoute
from urbanmove.permissions import *
from .serializers import CitySerializer, BusStopSerializer, BusRouteSerializer
from urbanmove.authentication import BearerAuthentication
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["City"],
)
class CityModelViewSet(viewsets.ModelViewSet):
    """
    Viewset that provides the standard actions for city
    """

    authentication_classes = [BearerAuthentication]
    permission_classes = [IsOperator]
    serializer_class = CitySerializer
    queryset = City.objects.all()
    http_method_names = ["get", "post", "delete", "put"]


@extend_schema(
    tags=["Bus Stop"],
)
class BustStopModelViewSet(viewsets.ModelViewSet):
    """
    Viewset that provides the standard actions for BusStop
    """

    authentication_classes = [BearerAuthentication]
    serializer_class = BusStopSerializer
    queryset = BusStop.objects.all()
    http_method_names = ["get", "post", "delete", "put"]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [IsPassagerOrOperator]
        else:
            permission_classes = [IsOperator]
        return [permission() for permission in permission_classes]


@extend_schema(
    tags=["Bus Routes"],
)
class BusRouteModalViewSet(viewsets.ModelViewSet):
    """
    Viewset that provides the standard actions for BusRoute
    """

    authentication_classes = [BearerAuthentication]
    serializer_class = BusRouteSerializer
    queryset = BusRoute.objects.all()
    http_method_names = ["get", "post", "delete", "put"]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [IsPassagerOrOperator]
        else:
            permission_classes = [IsOperator]
        return [permission() for permission in permission_classes]
