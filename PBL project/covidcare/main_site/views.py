from django.shortcuts import render, redirect
from .models import HospitalData
from .pinfilter import Pinfilter
from .forms import Form, Form1, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.


def Home_Page(request):
    context = {}
    return render(request, 'covid.html', context)


def Adding_Hospital_info(request):
    alpha = Form1()

    if request.method == 'POST':
        alpha = Form1(request.POST)
        if alpha.is_valid():
            alpha.save()

    context = {'alpha': alpha}
    return render(request, "AddingHospitalinfo.html", context)


def Hospital_info(request):
    gamma = HospitalData.objects.all()

    myqueryset = gamma
    pinfilter = Pinfilter(request.GET, queryset=myqueryset)
    myqueryset = pinfilter.qs
    form = Form()
    context = {"form": form, "myqueryset": myqueryset, "pinfilter": pinfilter}
    return render(request, "Hospitalinformation.html", context)


def Login_Page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("AddingHospitals")
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'loginpage.html')

    return render(request, "loginpage.html")


def RegisterationPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registeration.html', context)
