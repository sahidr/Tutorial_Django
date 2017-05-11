from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=200,unique=True,null=True)

    def __str__(self):
        return self.first_name