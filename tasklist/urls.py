from django.urls import include, path

from todo.urls import urlpatterns as todo_urls

urlpatterns = [
    path('', include('todo.urls')),
]
