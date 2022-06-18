


from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("sam", views.sam, name="sam"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet"),

]
