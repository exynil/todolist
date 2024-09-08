from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created_at", "status")
    list_display_links = ("id", "title")
    search_fields = ["id", "title"]


admin.site.register(Task, TaskAdmin)
