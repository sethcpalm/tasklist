from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from .models import TodoItem


class TodoView(ListView):
    model = TodoItem
    template_name = 'todo/index.html'


class TodoCreateView(CreateView):
    model = TodoItem
    success_url = '/'
    fields = ['description']


class TodoUpdateView(UpdateView):
    model = TodoItem
    success_url = '/'
    fields = ['description']


class TodoCompleteView(UpdateView):
    model = TodoItem
    success_url = '/'
    fields = ['status']


class TodoDeleteView(DeleteView):
    model = TodoItem
    success_url = '/'
