from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer
from .permissions import IsTaskOwnerOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = None
    permission_classes = [IsTaskOwnerOrReadOnly]

    # Добавляем фильтрацию по статусу и сортировку
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["status"]

    # Поля для сортировки
    ordering_fields = ["created_at", "status"]
    ordering = ["created_at"]

    def perform_create(self, serializer):
        """
        Сохраняет задачу с текущим пользователем в качестве владельца.
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Возвращает список задач для текущего пользователя.
        """
        user = self.request.user
        return Task.objects.filter(user=user)

    @action(methods=["patch"], detail=True, url_path="toggle-status")
    def toggle_status(self, request, pk):
        """
        Изменяет статус задачи между "активной" и "выполненной".
        """
        task = self.get_object()
        task.status = (
            Task.Status.ACTIVE
            if task.status == Task.Status.COMPLETED
            else Task.Status.COMPLETED
        )
        task.save()

        serializer = self.get_serializer(task)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
