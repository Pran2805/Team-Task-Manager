from django.db import models


class User(models.Model):
    username: str = models.CharField(max_length=255)
    email: str = models.EmailField(unique=True)
    password: str = models.CharField(max_length=255)