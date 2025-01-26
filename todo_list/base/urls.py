from base.views import TaskListView, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
   path('Login/', CustomLoginView.as_view(), name='login'),
   path('Logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
   path('', TaskListView.as_view(), name='tasks'),
   path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
   path('task-create/', TaskCreate.as_view(), name='task-create' ),
   path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update' ),
   path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete' ),
   path('Register/', RegisterPage.as_view(), name='register'),
   ]