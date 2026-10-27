from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Изучить Django")

        self.assertEqual(task.title, "Изучить Django")
        self.assertFalse(task.completed)


class TaskListViewTest(TestCase):
    def test_task_list_page_returns_200(self):
        response = self.client.get(reverse("task_list"))

        self.assertEqual(response.status_code, 200)

    def test_task_is_visible_on_page(self):
        Task.objects.create(title="Настроить CI")

        response = self.client.get(reverse("task_list"))

        self.assertContains(response, "Настроить CI")
