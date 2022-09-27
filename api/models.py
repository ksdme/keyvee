import uuid
from django.db import models


class Blob(models.Model):
    """
    Represents a blob on the keyvee platform.
    """

    namespace = models.UUIDField(default=uuid.uuid4, unique=True)

    key = models.CharField(max_length=128, db_index=True)
    value = models.JSONField(null=True, default=None, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("namespace", "key")
