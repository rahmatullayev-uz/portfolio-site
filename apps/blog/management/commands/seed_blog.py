from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.blog.models import BlogCategory, BlogPost, BlogTag


class Command(BaseCommand):
    help = "Namunaviy texnik maqolalar, toifalar va teglarni bazaga kiritadi"

    def handle(self, *args, **options):
        # 1. Toifalar
        cat_python, _ = BlogCategory.objects.get_or_create(
            name="Python & Django",
            defaults={"description": "Python tili va Django freymvorkidagi ilg'or amaliyotlar"},
        )
        cat_db, _ = BlogCategory.objects.get_or_create(
            name="Ma'lumotlar Bazasi & Kesh",
            defaults={"description": "PostgreSQL, Redis va SQL so'rovlar optimizatsiyasi"},
        )
        cat_devops, _ = BlogCategory.objects.get_or_create(
            name="DevOps & Arxitektura",
            defaults={"description": "Docker, CI/CD va yuqori yuklamali arxitekturalar"},
        )

        # 2. Teglar
        tag_django, _ = BlogTag.objects.get_or_create(name="django")
        tag_postgres, _ = BlogTag.objects.get_or_create(name="postgresql")
        tag_redis, _ = BlogTag.objects.get_or_create(name="redis")
        tag_docker, _ = BlogTag.objects.get_or_create(name="docker")
        tag_performance, _ = BlogTag.objects.get_or_create(name="performance")

        # 3. Maqolalar
        p1, created1 = BlogPost.objects.get_or_create(
            slug="django-orm-n-plus-1-optimization",
            defaults={
                "title": "Django ORM da N+1 Muammosi va Uni Select/Prefetch Yordamida Bartaraf Qilish",
                "category": cat_python,
                "summary": "Ko'p hollarda sekin ishlayotgan Django ilovalarining asosiy sababi N+1 so'rovlar muammosidir. Ushbu maqolada uni aniqlash va bartaraf etish usullarini ko'rib chiqamiz.",
                "content": """## Kirish

Django ORM juda qulay va tezkor ishlab chiqish imkoniyatini beradi, biroq bog'liq jadvallar bilan noto'g'ri ishlaganda ma'lumotlar bazasiga yuzlab ortiqcha SQL so'rovlar yuborilishi mumkin. Bu **N+1 muammosi** deb ataladi.

---

## N+1 Muammosi Qanday Yuzaga Keladi?

Tasavvur qiling, bizda `Project` va unga tegishli `Technology` modellari bor:

```python
# Noto'g'ri yondashuv (N+1 so'rov yuzaga keltiradi)
projects = Project.objects.all()

for project in projects:
    # Har bir iteratsiyada yangi SQL so'rovi ketadi!
    print(project.category.name)
```

Agar bazada 100 ta loyiha bo'lsa, bu kod **101 ta SQL so'rov** bajaradi!

---

## Yechim: `select_related` va `prefetch_related`

1. **`select_related`:** Bitta-birga (`OneToOne`) yoki Ko'pga-birga (`ForeignKey`) munosabatlarda `JOIN` orqali bitta so'rovda barcha ma'lumotlarni tortib oladi:

```python
# To'g'ri yondashuv (Faqat 1 ta SQL so'rov)
projects = Project.objects.select_related("category").all()
```

2. **`prefetch_related`:** Ko'pga-ko'p (`ManyToMany`) munosabatlarda qo'shimcha bitta `IN (...)` so'rovi bilan bog'liq yozuvlarni keshlaydi:

```python
# Faqat 2 ta SQL so'rov bajariladi
projects = Project.objects.prefetch_related("technologies").all()
```

---

## Xulosa

Murakkab ro'yxatlarni yaratishda har doim `select_related` va `prefetch_related` dan foydalaning. Bu ma'lumotlar bazasi yuklamasini 10 baravargacha yengillashtiradi.
""",
                "is_published": True,
                "published_at": timezone.now(),
            },
        )
        if created1:
            p1.tags.set([tag_django, tag_postgres, tag_performance])

        p2, created2 = BlogPost.objects.get_or_create(
            slug="redis-caching-strategies-django",
            defaults={
                "title": "Django Loyihalarida Redis Bilan Kesh Strategiyalari",
                "category": cat_db,
                "summary": "Redis keshidan to'g'ri foydalanish orqali API javob vaqtini soniyaning bir necha millisekundigacha tushirish usullari.",
                "content": """## Nega Aynan Redis?

Redis — xotirada (RAM) ishlovchi, ultra-tezkor kalit-qiymat (Key-Value) ma'lumotlar ombori. U quyidagi maqsadlar uchun ideal:
- Tezkashlanuvchi sahifalar va API javoblari
- Foydalanuvchi sessiyalari
- Rate-limiting (so'rovlar sonini cheklash)

---

## Django-Redis O'rnatish

```bash
uv add redis django-redis
```

`settings.py` da sozlash:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

---

## Keshni Avtomatik Tozalash (Cache Invalidation)

Yangi ma'lumot qo'shilganda eski keshni tozalash uchun Django signallaridan foydalanish eng toza yechimdir:

```python
from django.db.models.signals import post_save
from django.core.cache import cache

@receiver(post_save, sender=BlogPost)
def clear_blog_cache(sender, instance, **kwargs):
    cache.delete("blog_post_list")
```
""",
                "is_published": True,
                "published_at": timezone.now(),
            },
        )
        if created2:
            p2.tags.set([tag_redis, tag_django, tag_performance])

        self.stdout.write(self.style.SUCCESS("Namunaviy blog maqolalari kiritildi."))
