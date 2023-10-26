from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from urbanmove.core.api.views import CityModelViewSet
from urbanmove.users.api.views import UserAPI

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
router.register("city", CityModelViewSet)
urlpatterns = router.urls

urlpatterns += [
    path("users/register/", UserAPI.as_view(), name="register"),
]
