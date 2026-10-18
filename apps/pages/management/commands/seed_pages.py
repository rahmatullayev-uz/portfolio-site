from django.core.management.base import BaseCommand

from apps.pages.models import Experience, Profile, Skill


class Command(BaseCommand):
    help = "Boshlang'ich profil, ko'nikmalar va tajribalarni bazaga kiritadi"

    def handle(self, *args, **options):
        # 1. Profil
        profile, created = Profile.objects.get_or_create(
            id="00000000-0000-0000-0000-000000000001",
            defaults={
                "full_name": "Sardor Rahmatullayev",
                "title": "Senior Python & Backend Muhandis",
                "short_bio": "Yuqori unumdorlikka ega backend tizimlar, mikroservislar va zamonaviy veb-arxitekturalar yaratish bo'yicha mutaxassis.",
                "about_text": "Men Python, Django, FastAPI, PostgreSQL va Docker texnologiyalarida yuqori yuklamali tizimlarni loyihalash va ishlab chiqish bo'yicha ko'p yillik tajribaga egaman. Clean Architecture, TDD va avtomatlashtirilgan CI/CD jarayonlarini qo'llayman.",
                "email": "rahmatullayev207@gmail.com",
                "telegram_url": "https://t.me/rahmatullayev_uz",
                "github_url": "https://github.com/rahmatullayev",
                "linkedin_url": "https://linkedin.com/in/rahmatullayev",
                "years_of_experience": 4,
                "is_available_for_hire": True,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Asosiy profil yaratildi."))

        # 2. Ko'nikmalar
        skills_data = [
            ("Python", Skill.Category.BACKEND, "Ekspert", 1),
            ("Django & DRF", Skill.Category.BACKEND, "Ekspert", 2),
            ("FastAPI", Skill.Category.BACKEND, "Yuqori", 3),
            ("Celery & Redis", Skill.Category.BACKEND, "Yuqori", 4),
            ("PostgreSQL", Skill.Category.DATABASE, "Ekspert", 1),
            ("Redis", Skill.Category.DATABASE, "Yuqori", 2),
            ("SQL Optimizatsiya", Skill.Category.DATABASE, "Yuqori", 3),
            ("Docker & Compose", Skill.Category.DEVOPS, "Yuqori", 1),
            ("Linux & Nginx", Skill.Category.DEVOPS, "Yuqori", 2),
            ("CI/CD (GitHub Actions)", Skill.Category.DEVOPS, "O'rta", 3),
            ("Git & GitHub", Skill.Category.TOOLS, "Ekspert", 1),
            ("Tailwind CSS", Skill.Category.TOOLS, "Yuqori", 2),
            ("HTMX", Skill.Category.TOOLS, "Yuqori", 3),
        ]

        for name, category, prof, order in skills_data:
            Skill.objects.get_or_create(
                name=name, defaults={"category": category, "proficiency": prof, "order": order}
            )
        self.stdout.write(self.style.SUCCESS("Boshlang'ich ko'nikmalar yaratildi."))

        # 3. Tajriba
        experiences_data = [
            {
                "company": "Fintech & E-commerce Hub",
                "position": "Senior Backend Dasturchi",
                "company_url": "https://example.com",
                "start_date": "2023",
                "end_date": "Hozirgacha",
                "is_current": True,
                "description": "To'lov tizimlari bilan integratsiyalar, mikroservislar aloqasi, kesh va so'rovlar optimizatsiyasi.",
                "technologies_used": "Python, Django, FastAPI, PostgreSQL, Redis, Docker, Celery",
                "order": 1,
            },
            {
                "company": "IT Solutions & Software",
                "position": "Python / Django Dasturchi",
                "company_url": "https://example.com",
                "start_date": "2021",
                "end_date": "2023",
                "is_current": False,
                "description": "REST API xizmatlarini noldan ishlab chiqish, ma'lumotlar bazasi modellarini loyihalash va deploy qilish.",
                "technologies_used": "Python, Django, DRF, PostgreSQL, Nginx, Docker",
                "order": 2,
            },
        ]

        for exp in experiences_data:
            Experience.objects.get_or_create(
                company=exp["company"], position=exp["position"], defaults=exp
            )
        self.stdout.write(self.style.SUCCESS("Boshlang'ich tajribalar yaratildi."))
