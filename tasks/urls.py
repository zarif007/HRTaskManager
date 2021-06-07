from django.urls import path

from . import views

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('tasks', views.task_listings, name='task_listings'),
    path('tasks_history', views.task_history, name='task_history'),
    path('rank', views.user_rank, name='user_rank'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('create/', views.task_creation, name='task_creation'),
    path('member_list/', views.member_list, name='member_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task_done/<int:pk>/', views.task_done, name='task_done'),
    path('apply/<int:pk>/', views.task_apply, name='task_apply'),
    path('user/<int:pk>/', views.user_profile, name='user_profile'),
]