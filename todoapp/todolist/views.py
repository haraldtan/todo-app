from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoItem

# Create your views here.
def todoView(request):
    # get all items in the todoItem model
    allItems = todoItem.objects.all()
    # render todolist.html in templates folder
    return render(request, "todolist.html", 
        {'all_items': allItems}) # pass list to render

# handle POST request from todolist.html to add todo item
def addTodo(request):
    # create new todo item
    new_item = todoItem(content = request.POST['content'])
    # save
    new_item.save()
    # redirect browser to '/todolist/'
    return HttpResponseRedirect('/todolist/')

# handle POST request from todolist.html to delete todo item
def deleteTodo(request, todo_id):
    # retrieve todo object with todo_id
    item_to_delete = todoItem.objects.get(id=todo_id)
    # delete
    item_to_delete.delete()
    # redirect back
    return HttpResponseRedirect('/todolist/')