from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todoView, name='all'),
    path('add/', views.add, name='add'),
    path('<int:todo_id>', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:todo_id>/delete', views.delete, name='delete'),
]
