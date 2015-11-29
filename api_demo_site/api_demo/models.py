
from django.db import models


class Stuff(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1023, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        # Determines the order Stuff instances are returned in by querysets.
        ordering = ('-updated',)
