from django.db import models

class Task(models.Model):
    title = models.CharField("Название", max_length=200)
    completed = models.BooleanField("Выполнена", default=False)
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "задача"
        verbose_name_plural = "задачи"

    def __str__(self):
        return self.title
