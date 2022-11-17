from django.db import models

# Create your models here.
class message(models.Model):
    institute = models.CharField(max_length = 20)
    star = models.CharField(max_length = 20)
    comment = models.CharField(max_length = 100)
