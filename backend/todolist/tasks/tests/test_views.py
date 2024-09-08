from django.contrib.auth.models import User

from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from ..models import Task


class TaskViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.task = Task.objects.create(
            title="Тестовая задача",
            description="Описание задачи",
            user=self.user,
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        self.url = "/api/v1/tasks/"

    def test_get_task_list(self):
        # Получение списка задач
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Тестовая задача")

    def test_create_task(self):
        # Создание задачи
        data = {"title": "Новая задача", "description": "Описание новой задача"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Новая задача")

    def test_patch_task(self):
        # Изменение title задачи
        data = {"title": "Обновленная задача"}
        response = self.client.patch(f"{self.url}{self.task.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Обновленная задача")

    def test_delete_task(self):
        # Удаление задачи
        response = self.client.delete(f"{self.url}{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Проверка, что задача удалена
        response = self.client.get(f"{self.url}{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_toggle_status(self):
        # Начальный статус задачи
        self.assertEqual(self.task.status, Task.Status.ACTIVE)

        # Выполняем запрос на переключение статуса
        response = self.client.patch(f"{self.url}{self.task.id}/toggle-status/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что статус изменился на COMPLETED
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, Task.Status.COMPLETED)

        # Выполняем запрос снова для переключения обратно
        response = self.client.patch(f"{self.url}{self.task.id}/toggle-status/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что статус изменился обратно на ACTIVE
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, Task.Status.ACTIVE)
