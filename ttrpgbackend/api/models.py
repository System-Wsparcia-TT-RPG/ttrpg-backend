from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    level = models.IntegerField()
    