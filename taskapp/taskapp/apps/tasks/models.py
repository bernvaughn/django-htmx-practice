from django.db import models
from django.utils import timezone

class Task(models.Model):
    when = models.DateTimeField(
        null=False,
        blank=False,
        editable=False,
        default=timezone.now
    )
    title = models.TextField(
        null=False,
        blank=False,
        max_length=100
    )
    description = models.TextField(
        null=False,
        blank=False,
        max_length=1000
    )
    complete = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )
