import django_filters

from .models import HospitalData


class Pinfilter (django_filters.FilterSet):
    class Meta:
        model = HospitalData
        fields = ["Hospital_CityName","Hospital_Pincode","Hospital_ICUBeds","Hospital_ContactNo"]

