from django.urls import path
from  .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name="task"),
    path('task-creat/', TaskCreate.as_view(), name="task-create"),
]