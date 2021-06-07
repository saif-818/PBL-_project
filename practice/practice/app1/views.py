from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, "temp1.html")


def info(request):
    name = request.POST["Full name"]
    if int(request.POST["age"]) > 18:
        info1 = ("hello Sir/Madam")

    elif int(request.POST["age"]) < 18:
        info1 = "hello " + name

    return render(request, "info.html", {"res": name, "age": info1})
