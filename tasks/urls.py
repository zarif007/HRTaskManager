from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tasks', views.task_listings, name='task_listings'),
    path('create/', views.task_creation, name='task_creation'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('apply/<int:pk>/', views.task_apply, name='task_apply'),
]