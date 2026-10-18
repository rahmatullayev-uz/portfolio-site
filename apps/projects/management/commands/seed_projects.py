from django.core.management.base import BaseCommand

from apps.projects.models import Project, ProjectCategory, Technology


class Command(BaseCommand):
    help = "Namunaviy loyihalar, texnologiyalar va toifalarni bazaga kiritadi"

    def handle(self, *args, **options):
        # 1. Kategoriyalar
        cat_web, _ = ProjectCategory.objects.get_or_create(
            name="Veb Ilovalar", defaults={"description": "Full-stack veb ilovalar va platformalar"}
        )
        cat_api, _ = ProjectCategory.objects.get_or_create(
            name="Backend & API",
            defaults={"description": "Yuqori yuklamali REST va mikroservis tizimlar"},
        )
        cat_bot, _ = ProjectCategory.objects.get_or_create(
            name="Telegram Bot & Avtomatlashtirish",
            defaults={"description": "Asinxron botlar va integratsiyalar"},
        )

        # 2. Texnologiyalar
        tech_django, _ = Technology.objects.get_or_create(name="Django")
        tech_drf, _ = Technology.objects.get_or_create(name="DRF")
        tech_fastapi, _ = Technology.objects.get_or_create(name="FastAPI")
        tech_postgres, _ = Technology.objects.get_or_create(name="PostgreSQL")
        tech_redis, _ = Technology.objects.get_or_create(name="Redis")
        tech_docker, _ = Technology.objects.get_or_create(name="Docker")
        tech_celery, _ = Technology.objects.get_or_create(name="Celery")
        tech_tailwind, _ = Technology.objects.get_or_create(name="Tailwind CSS")

        # 3. Namunaviy Loyihalar
        p1, created1 = Project.objects.get_or_create(
            slug="fintech-payment-engine",
            defaults={
                "title": "Fintech To'lov va Tranzaksiyalar Dvigateli",
                "category": cat_api,
                "short_description": "Payme, Click va Stripe bilan integratsiya qilingan, soniyasiga 500+ tranzaksiyani xavfsiz qayta ishlaydigan backend tizimi.",
                "full_description": """## Loyiha Haqida

Ushbu tizim elektron tijorat va xizmat ko'rsatuvchi kompaniyalar uchun to'lovlarni xavfsiz va ishonchli amalga oshirishga mo'ljallangan.

### Asosiy Funksionalliklar:
- **Idempotency Keys:** Takroriy to'lovlarning oldini oluvchi kafolatlangan tranzaksiya mexanizmi.
- **Asinxron To'lov Tekshiruvlari:** Celery va Redis orqali webhook bildirishnomalarini real-time qayta ishlash.
- **Xavfsizlik:** HMAC imzo tekshiruvi va IP whitelist himoyasi.

```python
# To'lov imzosini tekshirish namunasi
import hmac
import hashlib

def verify_signature(payload: bytes, secret: str, received_signature: str) -> bool:
    computed = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, received_signature)
```

### Arxitektura:
Loyiha Docker konteynerlarida PostgreSQL, Redis va Django REST Framework negizida ishlaydi.
""",
                "github_url": "https://github.com/rahmatullayev",
                "live_demo_url": "https://example.com/demo1",
                "is_featured": True,
                "sort_order": 1,
            },
        )
        if created1:
            p1.technologies.set(
                [tech_django, tech_drf, tech_postgres, tech_redis, tech_celery, tech_docker]
            )

        p2, created2 = Project.objects.get_or_create(
            slug="ecommerce-highload-marketplace",
            defaults={
                "title": "Yuqori Yuklamali Savdo Platformasi",
                "category": cat_web,
                "short_description": "Katta hajmdagi tovarlar katalogi, elastik qidiruv va kesh tizimiga ega e-commerce platformasi.",
                "full_description": """## Loyiha Haqida

100,000+ mahsulotlar bazasini tezkor qidirish va filtrlash imkonini beruvchi zamonaviy internet-do'kon backend arxitekturasi.

### Natijalar:
- Redis kesh yordamida sahifa javob berish vaqti **45ms** gacha tushirildi.
- Murakkab SQL so'rovlar optimallashtirilib, DB yuklamasi 60% ga kamaytirildi.
""",
                "github_url": "https://github.com/rahmatullayev",
                "live_demo_url": "",
                "is_featured": True,
                "sort_order": 2,
            },
        )
        if created2:
            p2.technologies.set(
                [tech_django, tech_postgres, tech_redis, tech_tailwind, tech_docker]
            )

        p3, created3 = Project.objects.get_or_create(
            slug="telegram-crm-bot-platform",
            defaults={
                "title": "Avtomatlashtirilgan Telegram CRM Bot",
                "category": cat_bot,
                "short_description": "Mijozlar buyurtmalarini qabul qiluvchi, operatorlarga yo'naltiruvchi va to'lovlarni bot ichida qabul qiluvchi tizim.",
                "full_description": """## Loyiha Haqida

Kichik va o'rta bizneslar uchun xizmat va mahsulotlarni Telegram orqali avtomatik sotish tizimi.

### Xususiyatlar:
- Webhook orqali ultra-tezkor asinxron javob vaqti.
- Operatorlar uchun web admin paneli.
""",
                "github_url": "https://github.com/rahmatullayev",
                "live_demo_url": "https://t.me/example_bot",
                "is_featured": True,
                "sort_order": 3,
            },
        )
        if created3:
            p3.technologies.set([tech_fastapi, tech_postgres, tech_redis, tech_docker])

        self.stdout.write(self.style.SUCCESS("Namunaviy loyihalar va texnologiyalar kiritildi."))
