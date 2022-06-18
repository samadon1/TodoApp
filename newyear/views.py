import datetime
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def eve(request):
    now = datetime.datetime.now()
    
        
    
    context = {"date": now, "christamas": True}
    return render(request, 'newyear/index.html', context)