from django.db import models
from django.utils import timezone
from django_eventstream import send_event

class Task(models.Model):
    when = models.DateTimeField(
        null=False,
        blank=False,
        editable=False,
        default=timezone.now
    )
    title = models.CharField(
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

    def save(self, *args, **kwargs):
        # save the instance
        super().save(*args, **kwargs)

        # send on the channel
        send_event(
            'task-updates-channel',
            f'saved-task-{self.id}',
            {
                'id': self.id
            }
        )
