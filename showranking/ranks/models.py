from django.db import models

class Ranks(models.Model):
    username = models.CharField(max_length=255)
    ranking = models.IntegerField(default=0)
