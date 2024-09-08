from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1, " Задача находится в процессе выполнения или ожидает начала"
        COMPLETED = 2, "Задача завершена"

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Создан",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Изменён",
        auto_now=True,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        choices=Status.choices,
        default=1,
        blank=True,
    )
    user = models.ForeignKey(
        to=User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
