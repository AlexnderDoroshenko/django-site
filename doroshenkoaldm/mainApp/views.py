from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainApp/homePage.html')

def blog(request):
    return render(request, 'mainApp/includes/someHtml.html')