# todo_list/todo_app/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ToDoList, ToDoItem
from django.urls import reverse, reverse_lazy

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    
class ListDelete(DeleteView):
    model = ToDoList
    # You have to use reverse_lazy() instead of reverse(),
    # as the urls are not loaded when the file is imported.
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context