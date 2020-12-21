from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def interfaceSum(request):
    """接口集合"""
    return render(request, 'interfaceSum.html')
