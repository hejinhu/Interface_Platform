from django.shortcuts import render
from Platform import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def interfaceSum(request):
    """接口集合"""
    team = models.interface.objects.all()
    return render(request, 'interfaceSum.html', {'team': team})
