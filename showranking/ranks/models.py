from django.db import models

class Ranks(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
