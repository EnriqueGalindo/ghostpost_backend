from django.db import models
from django.utils import timezone


class Post(models.Model):
    bost_or_roast = models.BooleanField()
    message = models.CharField(max_length=280)
    popularity = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message