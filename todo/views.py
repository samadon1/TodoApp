from django.shortcuts import render
from django import forms

# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def tasks(request):
    if "items" not in request.session:
        request.session["items"] = []
    


    context = {"tasks": request.session["items"]}
    return render(request, 'todo/tasks.html', context )


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["items"] += [task] 
        else:
            return render(request, 'todo/index.html', {'form': form})
    return render(request, 'todo/index.html', {"form": NewTaskForm()})