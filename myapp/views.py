from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import tododb
from .forms import todoform

# Create your views here.





def index (request):
    tasks = tododb.objects.all()
    form=todoform()
    if request.method == "POST":
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'tasks':tasks, 'form':form}
    return render(request,"index.html",context)

def updatetodo(request,pk):
    task=tododb.objects.get(id=pk)
    form =todoform(instance=task)
    if request.method == "POST":
        form = todoform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect(index)

    context={'form':form}
    return render(request,"update.html",context)

def removetask(request,pk):
    item = tododb.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect(index)
    context = {'item':item}
    return render(request,"remove.html",context)

