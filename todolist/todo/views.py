from django.shortcuts import render,redirect
from.models import TodoList

# Create your views here.
def todolist(request):
    mytodo = TodoList.objects.all()
    context = {
        "mytodos" : mytodo
    }
    return render(request, "index.html", context)

def addtask(request):
    mytask = request.POST['task']
    TodoList(task = mytask).save()
    return redirect(request.META['HTTP_REFERER'])

def deletask(request, taskpk):
    TodoList.objects.filter(id = taskpk).delete()
    return redirect(request.META['HTTP_REFERER'])