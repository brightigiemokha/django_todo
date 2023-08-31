from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name="task"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('task-create/', TaskCreate.as_view(), name="todo-create"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="todo-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="todo-update"),
    path('task-delete/', TaskDelete.as_view(), name="todo-delete"),
]