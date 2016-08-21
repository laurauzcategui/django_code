from django.shortcuts import render
from . models import Location

def home(request):
    locations = Location.objects.all()
    return render(request, 'home.html',{'locations':locations})
