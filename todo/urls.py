from django.urls import path

from .views import TodoView, TodoCreateView, TodoUpdateView, TodoCompleteView, TodoDeleteView

urlpatterns = [
    path('', TodoView.as_view(), name='index'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('edit/<pk>/', TodoUpdateView.as_view(), name='edit'),
    path('complete/<pk>/', TodoCompleteView.as_view(), name='complete'),
    path('delete/<pk>/', TodoDeleteView.as_view(), name='delete'),
]

