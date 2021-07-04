from django.db import models


# Create your models here.
class HospitalData(models.Model):
    Hospital_Name = models.CharField(max_length=30)
    Hospital_CityName = models.CharField(max_length=15)
    Hospital_Pincode = models.BigIntegerField()
    Hospital_ICUBeds= models.BooleanField()
    Hospital_ContactNo = models.BigIntegerField()


