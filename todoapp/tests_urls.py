from django.test import TestCase
from django.urls import reverse, resolve
from todoapp.views import TaskDetail, TaskUpdate, TaskDelete, TaskCreate, TaskList


class TestUrls(TestCase):

    def test_task_urls_is_required(self):
        url = reverse('task')
        print(resolve(url))
        self.assertEqual(resolve(url).clas, TaskList )