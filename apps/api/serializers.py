from rest_framework import serializers

from apps.api.models import Kanban, Board, Subtask


class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = (
            'name',
            'desc',
            'status',
            'subtasks',
            'created_at',
            'updated_at'
        )


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'name',
            'column',
            'created_at',
            'updated_at'
        )


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = (
            'name',
            'created_at',
            'updated_at'
        )
