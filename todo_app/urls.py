from django.urls import path
from todo_app import views



urlpatterns = [
    path('tasklist', views.task_list, name='task_list'),
    path('add', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_completion, name='toggle_completion'),
    path('login',views.loginView,name="login"),
    path('register',views.register,name='register'),
    path('logout',views.logoutView,name='logout'),
    path('',views.authpage,name='logout'),
]
