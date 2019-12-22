from django.urls import path
from todo import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('history/', views.history, name='history'),
    path('contributions/', views.contributions, name='contributions'),
    path('addTodo/', views.addTodo, name="addTodo"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name="deleteTodo"),
    path('archiveTodo/<int:todo_id>/', views.archiveTodo, name="archiveTodo"),
]