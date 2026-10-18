import bleach
import markdown
from django.db import models
from django.utils.text import slugify

from apps.common.models import TimeStampedModel


class Technology(TimeStampedModel):
    """
    Loyiha texnologiyalari (masalan: Django, PostgreSQL, Docker, Redis).
    """

    name = models.CharField(max_length=80, unique=True, verbose_name="Texnologiya nomi")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    badge_color = models.CharField(max_length=30, default="emerald", verbose_name="Rang (Tailwind)")

    class Meta:
        ordering = ["name"]
        verbose_name = "Texnologiya"
        verbose_name_plural = "Texnologiyalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProjectCategory(TimeStampedModel):
    """
    Loyihalar toifasi (Web, API & Backend, Open Source, Telegram Bot).
    """

    name = models.CharField(max_length=100, unique=True, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Kategoriya tavsifi")

    class Meta:
        ordering = ["name"]
        verbose_name = "Loyiha toifasi"
        verbose_name_plural = "Loyiha toifalari"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    """
    Asosiy loyiha modeli.
    """

    title = models.CharField(max_length=200, verbose_name="Loyiha sarlavhasi")
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.TextField(
        max_length=350,
        verbose_name="Qisqa tavsif (kartochka uchun)",
        help_text="Loyihaning asosiy maqsadi va vazifasini 1-2 jumlada ifodalang.",
    )
    full_description = models.TextField(
        verbose_name="Batafsil tavsif (Markdown formatida)",
        help_text="Loyiha arxitekturasi, yechilgan muammolar, API tuzilishi va ishlatilgan yondashuvlar.",
    )
    cover_image = models.ImageField(
        upload_to="projects/covers/", blank=True, null=True, verbose_name="Muqova rasmi"
    )

    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects",
        verbose_name="Kategoriya",
    )
    technologies = models.ManyToManyField(
        Technology, blank=True, related_name="projects", verbose_name="Ishlatilgan texnologiyalar"
    )

    github_url = models.URLField(blank=True, verbose_name="GitHub havola")
    live_demo_url = models.URLField(blank=True, verbose_name="Jonli demo / Sayt havola")

    is_featured = models.BooleanField(
        default=False, verbose_name="Bosh sahifada ko'rsatilsinmi? (Featured)"
    )
    sort_order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def get_description_html(self):
        """
        Markdown matnni xavfsiz HTML ko'rinishiga aylantirish.
        """
        raw_html = markdown.markdown(
            self.full_description,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.toc",
                "markdown.extensions.tables",
            ],
        )
        # XSS xavfini oldini olish uchun ruxsat etilgan teglar
        allowed_tags = bleach.ALLOWED_TAGS.union(
            [
                "p",
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "pre",
                "code",
                "span",
                "div",
                "table",
                "thead",
                "tbody",
                "tr",
                "th",
                "td",
                "img",
                "hr",
                "br",
                "blockquote",
                "ul",
                "ol",
                "li",
                "strong",
                "em",
                "a",
            ]
        )
        allowed_attrs = {
            "*": ["class", "id"],
            "a": ["href", "title", "target", "rel"],
            "img": ["src", "alt", "title"],
        }
        return bleach.clean(raw_html, tags=allowed_tags, attributes=allowed_attrs)
