from django.views.generic import ListView, DeleteView

from .models import TodoItem


class TodoView(ListView):
    model = TodoItem
    template_name = 'todo/index.html'


class TodoDeleteView(DeleteView):
    model = TodoItem
