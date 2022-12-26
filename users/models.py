from django.db import models
from django.utils import timezone

# Create your models here.

class UsersPassword(models.Model):
    id = models.IntegerField(primary_key=True)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    @property
    def is_authenticated(self):
        return True
    
    

    
