from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from urbanmove.core.api.views import (
    CityModelViewSet,
    BustStopModelViewSet,
    BusRouteModalViewSet,
)
from urbanmove.users.api.views import UserAPI, UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
router.register("users", UserViewSet)
router.register("cities", CityModelViewSet)
router.register("stops", BustStopModelViewSet)
router.register("routes", BusRouteModalViewSet)
urlpatterns = router.urls

urlpatterns += [
    path("register/", UserAPI.as_view(), name="register"),
]
