import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    Barcha modellar uchun umumiy yaratilgan va yangilangan vaqtni saqlovchi abstrakt model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        abstract = True
