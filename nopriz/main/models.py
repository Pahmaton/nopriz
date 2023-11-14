from django.db import models

class User(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)