from django.urls import path
from . import views


urlpatterns= [path('', views.Home_Page, name='home'),
              path("hospitalinfo", views.Hospital_info,name='hospitalinfo'),
              path('login', views.Login_Page, name='login'),
              path('register', views.RegisterationPage, name='register'),
              path('AddingHospitals', views.Adding_Hospital_info, name='AddingHospitals')]