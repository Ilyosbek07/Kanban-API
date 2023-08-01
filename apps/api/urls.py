from django.urls import path

from apps.api.views import (
    KanbanListMV,
    KanbanDetailMV,

    SubtaskListMV,
    SubtaskDetailMV,

    BoardListMV,
    BoardDetailMV,
)

urlpatterns = [
    path('', KanbanListMV.as_view()),
    path('<int:pk>/', KanbanDetailMV.as_view()),

    # SubTask API
    path('subtask/', SubtaskListMV.as_view()),
    path('subtask/<int:pk>/', SubtaskDetailMV.as_view()),

    # Board API
    path('board/', BoardListMV.as_view()),
    path('board/<int:pk>/', BoardDetailMV.as_view())
]
