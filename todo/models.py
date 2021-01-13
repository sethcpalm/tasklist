from django.db import models


class TodoItem(models.Model):

    STATUSES = [
        ('PENDING', 'Pending'),
        ('COMPLETE', 'COMPLETE')
    ]

    description = models.CharField(max_length=32)
    status = models.CharField(max_length=8, choices=STATUSES)
