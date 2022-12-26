# Generated by Django 4.1.4 on 2022-12-25 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0008_delete_userspasswordf_passenger_public"),
    ]

    operations = [
        migrations.CreateModel(
            name="UsersPasswordf",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("is_active", models.IntegerField(default=1)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(default=django.utils.timezone.now)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("password", models.CharField(max_length=30)),
            ],
        ),
    ]
