from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem, ArchivedItem


# Create your views here.
def todo(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, "todo.html",
    {'all_items': all_todo_items})

def history(request):
    all_archived_items = ArchivedItem.objects.all()
    return render(request, "history.html", 
    {'all_archived_items': all_archived_items})

def contributions(request):
    return render(request, "contributions.html")

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_archive_item = ArchivedItem(content = new_item.content , time = new_item.time, info = "Added on") 
    new_item.save()
    new_archive_item.save()
    return HttpResponseRedirect('/todo/')
   

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    new_archive_item = ArchivedItem(content = new_item.content , time = new_item.time) 
    new_item.save()
    return HttpResponseRedirect('/todo/')

def archiveTodo(request, todo_id):
    item_to_archive = TodoItem.objects.get(id=todo_id)
    new_archive_item = ArchivedItem(content = item_to_archive.content , time = item_to_archive.time, info = "Deleted on")
    new_archive_item.save()
    item_to_archive.delete()
    return HttpResponseRedirect('/todo/')
  
	


	
