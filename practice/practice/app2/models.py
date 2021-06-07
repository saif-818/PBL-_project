from django.db import models


# Create your models here.
class Pinfornmation(models.Model):
    Name = models.CharField(max_length=40)
    MobileNumber = models.IntegerField()
    Pin = models.IntegerField()
    Age = models.IntegerField()


