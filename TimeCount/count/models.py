from django.db import models

# Create your models here.
class timecount(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    classroom = models.CharField(max_length=10)
    writer = models.CharField(max_length=10)
    timezone = models.CharField(max_length=10)