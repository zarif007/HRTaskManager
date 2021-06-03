from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_listings, name='task_listings'),
    path('create/', views.task_creation, name='task_creation'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]