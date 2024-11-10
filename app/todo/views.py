from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoList(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'

class TodoCreate(CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoUpdate(UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoDelete(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')

