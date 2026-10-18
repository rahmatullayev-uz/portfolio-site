from django.db import models

from apps.common.models import TimeStampedModel


class ContactMessage(TimeStampedModel):
    """
    Sayt orqali yuborilgan aloqa xabarlari modeli.
    """

    sender_name = models.CharField(max_length=120, verbose_name="Yuboruvchi ismi")
    sender_email = models.EmailField(verbose_name="Yuboruvchi emaili")
    subject = models.CharField(max_length=200, blank=True, verbose_name="Xabar mavzusi")
    message = models.TextField(verbose_name="Xabar matni")

    ip_address = models.GenericIPAddressField(
        blank=True, null=True, verbose_name="Yuboruvchi IP manzili"
    )
    is_read = models.BooleanField(default=False, verbose_name="O'qilganmi?")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Aloqa xabari"
        verbose_name_plural = "Aloqa xabarlari"

    def __str__(self):
        return f"{self.sender_name} - {self.subject or 'Mavzusiz'}"
