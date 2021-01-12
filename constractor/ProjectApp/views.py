from django.shortcuts import render
from . import views

# Create your views here.


def service(request):
    return render(request, 'services-1.html')