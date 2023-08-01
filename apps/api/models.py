from django.db import models
from apps.common.models import BaseModel

STATUS = (
    ('TODO', 'TODO'),
    ('DOING', 'DOING'),
    ('DONE', 'DONE')
)


class Subtask(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Kanban(BaseModel):
    # name = models.CharField(max_length=255, verbose_name=_('name'))
    # desc = models.TextField(verbose_name=_('desc'))
    # status = models.CharField(max_length=15, choices=STATUS,verbose_name=_('status'))
    name = models.CharField(max_length=255)
    desc = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS)

    subtasks = models.ManyToManyField(
        Subtask,
        related_name='subtask'
    )

    def __str__(self):
        return self.name


class Board(BaseModel):
    name = models.CharField(max_length=255)
    column = models.ManyToManyField(
        Kanban,
        related_name='kanban_column'
    )

    def __str__(self):
        return self.name
