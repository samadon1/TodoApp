from django.urls import path
from . import views


urlpatterns = [ 
    path("", views.eve, name='index')
]