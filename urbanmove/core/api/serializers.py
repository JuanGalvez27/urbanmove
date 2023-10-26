from rest_framework import serializers

from urbanmove.core.models import BusRoute, BusStop, City, StopSchedule


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = City
        fields = ["name"]


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = ["name", "latitude", "longitude", "city"]
