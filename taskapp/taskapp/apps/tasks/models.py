from django.db import models
from django.utils import timezone

class Task(models.Model):
    when = models.DateTimeField(
        null=False,
        blank=False,
        editable=False,
        default=timezone.now
    )
    description = models.TextField(
        null=False,
        blank=False,
        max_length=1000
    )