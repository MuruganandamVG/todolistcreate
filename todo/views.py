from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    todolist=Todo.objects.all()
    if request.method == 'POST':
        new_todo=Todo(title=request.POST['title'])
        new_todo.save()
        return redirect('/')

    return render(request,'index.html',{'todo':todolist})
def delete(request,pk):
    todolist=Todo.objects.get(id=pk)
    todolist.delete()
    return redirect('/')