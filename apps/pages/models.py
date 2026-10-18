from django.db import models

from apps.common.models import TimeStampedModel


class Profile(TimeStampedModel):
    """
    Muallif haqidagi asosiy ma'lumotlar modeli (Singleton tarzida 1 ta yozuv).
    """

    full_name = models.CharField(
        max_length=150, verbose_name="To'liq ism", default="Sardor Rahmatullayev"
    )
    title = models.CharField(
        max_length=200, verbose_name="Kasb / Unvon", default="Senior Python / Backend Muhandis"
    )
    short_bio = models.TextField(
        verbose_name="Qisqa bio (Hero qismi uchun)",
        default="Yuqori unumdorlikka ega backend tizimlar, mikroservislar va zamonaviy veb-arxitekturalar yaratish bo'yicha mutaxassis.",
    )
    about_text = models.TextField(
        verbose_name="Batafsil ma'lumot (Men haqimda sahifasi uchun)",
        default="Men Python, Django, FastAPI, PostgreSQL va Docker texnologiyalarida yuqori yuklamali tizimlarni loyihalash va ishlab chiqish bo'yicha tajribaga egaman.",
    )
    avatar = models.ImageField(
        upload_to="profile/", blank=True, null=True, verbose_name="Avatar rasmi"
    )
    resume_file = models.FileField(
        upload_to="resumes/", blank=True, null=True, verbose_name="Rezyume (CV PDF)"
    )

    # Ijtimoiy tarmoqlar
    email = models.EmailField(default="rahmatullayev207@gmail.com", verbose_name="Email")
    telegram_url = models.URLField(
        blank=True, default="https://t.me/rahmatullayev_uz", verbose_name="Telegram"
    )
    github_url = models.URLField(
        blank=True, default="https://github.com/rahmatullayev", verbose_name="GitHub"
    )
    linkedin_url = models.URLField(
        blank=True, default="https://linkedin.com/in/rahmatullayev", verbose_name="LinkedIn"
    )

    # Qo'shimcha parametrlar
    years_of_experience = models.PositiveIntegerField(default=4, verbose_name="Tajriba yillari")
    is_available_for_hire = models.BooleanField(
        default=True, verbose_name="Yangi takliflarga ochiqmi?"
    )

    class Meta:
        verbose_name = "Profil ma'lumotlari"
        verbose_name_plural = "Profil ma'lumotlari"

    def __str__(self):
        return self.full_name


class Skill(TimeStampedModel):
    """
    Ko'nikmalar va texnologiyalar modeli.
    """

    class Category(models.TextChoices):
        BACKEND = "backend", "Backend"
        DATABASE = "database", "Ma'lumotlar Bazasi"
        DEVOPS = "devops", "DevOps & Bulut"
        TOOLS = "tools", "Asboblar & Frontend"

    name = models.CharField(max_length=100, verbose_name="Ko'nikma nomi")
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.BACKEND, verbose_name="Kategoriya"
    )
    proficiency = models.CharField(
        max_length=50,
        blank=True,
        default="Yuqori daraja",
        verbose_name="Daraja (masalan: Advanced, Proficient)",
    )
    icon_name = models.CharField(
        max_length=100, blank=True, verbose_name="SVG yoki Lucide ikonkasi nomi"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Experience(TimeStampedModel):
    """
    Ish tajribasi xronologiyasi modeli.
    """

    company = models.CharField(max_length=150, verbose_name="Kompaniya / Tashkilot")
    position = models.CharField(max_length=150, verbose_name="Lavozim")
    company_url = models.URLField(blank=True, verbose_name="Kompaniya sayti")
    start_date = models.CharField(
        max_length=50, verbose_name="Boshlangan vaqt (masalan: Yanvar 2022)"
    )
    end_date = models.CharField(
        max_length=50, blank=True, default="Hozirgacha", verbose_name="Tugagan vaqt"
    )
    is_current = models.BooleanField(default=False, verbose_name="Hozirda shu yerda ishlayapman")
    description = models.TextField(verbose_name="Vazifalar va yutuqlar tavsifi")
    technologies_used = models.CharField(
        max_length=255, blank=True, verbose_name="Ishlatilgan texnologiyalar (vergul bilan)"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Ish tajribasi"
        verbose_name_plural = "Ish tajribalari"

    def __str__(self):
        return f"{self.position} - {self.company}"
