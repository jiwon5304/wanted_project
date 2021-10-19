from django.db import models
from django.db.models.deletion import CASCADE

from core.models import TimeStamp

class Post(TimeStamp):
    author = models.ForeignKey("users.User", on_delete=CASCADE)
    subjects = models.CharField(max_length=100)
    contents = models.TextField(null=True)

    class Meta:
        db_table = "posts"