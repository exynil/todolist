from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet


router = routers.SimpleRouter()

router.register(r"", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
