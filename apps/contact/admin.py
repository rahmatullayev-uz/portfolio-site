from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("sender_name", "sender_email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("sender_name", "sender_email", "subject", "message")
    readonly_fields = (
        "sender_name",
        "sender_email",
        "subject",
        "message",
        "ip_address",
        "created_at",
        "updated_at",
    )

    def has_add_permission(self, request):
        return False  # Xabarlar faqat tashqaridan keladi
