from django.urls import path
from  .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/', DeleteView.as_view(), name='task-delete'),
]