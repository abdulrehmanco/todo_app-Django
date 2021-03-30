from django.shortcuts import render, HttpResponse,redirect
from .models import *
from .forms import *

def homepage(request):
    todo = todoform.objects.all()
    form = formtodo()
    if request.method=='POST':
        form = formtodo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    context={'todo':todo,'form':form}
    return render (request,'home.html',context)

def updatetask(request, pk):
    todos=todoform.objects.get(id=pk)
    form = formtodo(instance=todos)
    if request.method=="POST":
          form = formtodo(request.POST, instance=todos)
          if form.is_valid():
              form.save()
              return redirect('/')   

    context={'form':form}
    return render(request, 'update.html',context)
    
def deletetask(request, pk):
    item = todoform.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request, 'delete.html', context)