from django.urls import path

from apps.api.views import KanbanListMV, KanbanDetailMV

urlpatterns = [
    path('', KanbanListMV.as_view()),
    path('<int:pk>/', KanbanDetailMV.as_view())
]
