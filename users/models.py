from django.db import models
from core.models import TimeStamp


class User(TimeStamp):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    

    class Meta:
        db_table = "users"
