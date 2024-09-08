from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Task


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.task = Task.objects.create(
            title="Тестовая задача",
            description="Описание задачи",
            user=self.user,
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Тестовая задача")
        self.assertEqual(self.task.status, Task.Status.ACTIVE)


    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Тестовая задача")
