from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")

def sam(request):
    return HttpResponse("Hello Sam")

def david(request):
    return HttpResponse("Hello David")

def greet(request, name):
    context = {"name" : name}
    return render(request, "hello/greet.html", context)

