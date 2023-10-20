from django.db import models


class City(models.Model):
    name = models.CharField(max_length=150, verbose_name=("City"), blank=False)


class BusStop(models.Model):
    name = models.CharField(max_length=150, verbose_name=("Bus Stop"), blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.ForeignKey(City, verbose_name=("City"), on_delete=models.CASCADE)


class BusRoute(models.Model):
    name = models.CharField(max_length=150, verbose_name=("Bus Route"), blank=False)
    origin = models.CharField(max_length=150, verbose_name=("Origin"), blank=False)
    destination = models.CharField(max_length=150, verbose_name=("Destination"), blank=False)


class Days(models.TextChoices):
    MONDAY = 0, "monday"
    TUESDAY = 1, "tuesday"
    WEDNESDAY = 2, "wednesday"
    THURSDAY = 3, "thursday"
    FRIDAY = 4, "friday"
    SATURADAY = 5, "saturday"
    SUNDAY = 6, "sunday"


class StopSchedule(models.Model):
    day = models.CharField(
        verbose_name=("Weekday"),
        choices=Days.choices,
        max_length=15,
        null=True,
        default=None,
    )
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    bus_stop = models.ForeignKey(BusStop, verbose_name=("Bus Stop"), on_delete=models.CASCADE)
    bus_route = models.ForeignKey(BusRoute, verbose_name=("Bus Route"), on_delete=models.CASCADE)
