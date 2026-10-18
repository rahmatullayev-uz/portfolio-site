from django.contrib import messages
from django.shortcuts import render

from .forms import ContactForm
from .services import send_telegram_notification


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def contact_view(request):
    is_success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            contact_msg.ip_address = get_client_ip(request)
            contact_msg.save()

            # Telegram bot orqali bildirishnoma yuborish
            send_telegram_notification(contact_msg)

            is_success = True
            messages.success(
                request, "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanaman."
            )

            if request.headers.get("HX-Request"):
                return render(request, "contact/partials/success_message.html")

            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        "form": form,
        "is_success": is_success,
    }
    return render(request, "contact/contact.html", context)
