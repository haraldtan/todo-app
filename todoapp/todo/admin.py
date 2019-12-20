from django.contrib import admin
from todo.models import TodoItem

# Register your models here.
class todoAdmin(admin.ModelAdmin):
    pass

admin.site.register(TodoItem, todoAdmin)