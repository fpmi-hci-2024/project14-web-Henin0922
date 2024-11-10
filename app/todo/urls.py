from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('create/', views.TodoCreate.as_view(), name='todo_create'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name='todo_update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete'),
]

