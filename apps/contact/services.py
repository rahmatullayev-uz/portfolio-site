import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_telegram_notification(message_obj):
    """
    Yangi kelgan aloqa xabari haqida Telegram bot orqali admin profiliga xabar yuborish.
    Xatolik yuz bersa ham asosiy jarayon to'xtatilmaydi.
    """
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", None)
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", None)

    if not token or not chat_id:
        # Telegram token yoki chat ID belgilanmagan
        return False

    text = (
        f"📬 <b>Yangi Xabar (Rahmatullayev.uz)</b>\n\n"
        f"👤 <b>Yuboruvchi:</b> {message_obj.sender_name}\n"
        f"📧 <b>Email:</b> {message_obj.sender_email}\n"
        f"📌 <b>Mavzu:</b> {message_obj.subject or 'Mavzusiz'}\n\n"
        f"💬 <b>Xabar:</b>\n{message_obj.message}"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        response = requests.post(url, json=payload, timeout=3.5)
        response.raise_for_status()
        return True
    except Exception as exc:
        logger.warning(f"Telegram botga xabar yuborishda xatolik: {exc}")
        return False
