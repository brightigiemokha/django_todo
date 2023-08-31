from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView

urlpatterns = [
    path('', TaskList.as_view(), name="task"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('task-create/', TaskCreate.as_view(), name="todo-create"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="todo-detail"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="todo-update"),
    path('task-delete/', TaskDelete.as_view(), name="todo-delete"),
]