# Generated by Django 4.2.6 on 2023-10-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_user_first_name_user_last_name_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("operator", "Operator"), ("passenger", "Passenger")],
                default="passenger",
                max_length=10,
            ),
        ),
    ]
