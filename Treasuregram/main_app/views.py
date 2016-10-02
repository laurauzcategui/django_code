from django.shortcuts import render
from . models import Treasure


def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})
