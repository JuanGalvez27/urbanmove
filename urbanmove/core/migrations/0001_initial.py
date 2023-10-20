# Generated by Django 4.2.6 on 2023-10-20 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BusRoute",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Bus Route")),
                ("origin", models.CharField(max_length=150, verbose_name="Origin")),
                ("destination", models.CharField(max_length=150, verbose_name="Destination")),
            ],
        ),
        migrations.CreateModel(
            name="BusStop",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="Bus Stop")),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="City")),
            ],
        ),
        migrations.CreateModel(
            name="StopSchedule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("0", "monday"),
                            ("1", "tuesday"),
                            ("2", "wednesday"),
                            ("3", "thursday"),
                            ("4", "friday"),
                            ("5", "saturday"),
                            ("6", "sunday"),
                        ],
                        default=None,
                        max_length=15,
                        null=True,
                        verbose_name="Weekday",
                    ),
                ),
                ("arrival_time", models.TimeField()),
                ("departure_time", models.TimeField()),
                (
                    "bus_route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.busroute", verbose_name="Bus Route"
                    ),
                ),
                (
                    "bus_stop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.busstop", verbose_name="Bus Stop"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="busstop",
            name="city",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.city", verbose_name="City"),
        ),
    ]
