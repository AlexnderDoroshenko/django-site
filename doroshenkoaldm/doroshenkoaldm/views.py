from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainApp/homePage.html')


def cv(request):
    return render(request, 'mainApp/includes/cvTemplate.html')


def cs(request):
    return render(request, 'mainApp/includes/Car_service.html')