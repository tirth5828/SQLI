# Generated by Django 4.1.4 on 2022-12-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flights", "0007_userspasswordf"),
    ]

    operations = [
        migrations.DeleteModel(name="UsersPasswordf",),
        migrations.AddField(
            model_name="passenger",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
