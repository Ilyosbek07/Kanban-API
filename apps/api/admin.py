from django.contrib import admin

from apps.api.models import Kanban, Board, Subtask

admin.site.register(Kanban)
admin.site.register(Board)
admin.site.register(Subtask)
