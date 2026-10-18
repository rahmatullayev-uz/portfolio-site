import math

import bleach
import markdown
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from apps.common.models import TimeStampedModel


class BlogCategory(TimeStampedModel):
    """
    Maqolalar toifasi (masalan: Python, Django, DevOps, Ma'lumotlar Bazasi, Karyera).
    """

    name = models.CharField(max_length=100, unique=True, verbose_name="Toifa nomi")
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Toifa tavsifi")

    class Meta:
        ordering = ["name"]
        verbose_name = "Blog toifasi"
        verbose_name_plural = "Blog toifalari"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogTag(TimeStampedModel):
    """
    Maqola teglari (masalan: #django, #redis, #docker, #performance).
    """

    name = models.CharField(max_length=60, unique=True, verbose_name="Teg nomi")
    slug = models.SlugField(max_length=80, unique=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"#{self.name}"


class BlogPost(TimeStampedModel):
    """
    Texnik maqolalar va blog postlar modeli.
    """

    title = models.CharField(max_length=220, verbose_name="Maqola sarlavhasi")
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    summary = models.TextField(
        max_length=400,
        verbose_name="Qisqacha xulosa (meta tavsif va kartochka uchun)",
        help_text="Maqola mazmunini 1-2 jumlada bayon qiling.",
    )
    content = models.TextField(
        verbose_name="Maqola matni (Markdown formatida)",
        help_text="Markdown formatida yozing. Kod bloklari uchun ```python ... ``` dan foydalaning.",
    )
    cover_image = models.ImageField(
        upload_to="blog/covers/", blank=True, null=True, verbose_name="Muqova rasmi"
    )

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Toifa",
    )
    tags = models.ManyToManyField(BlogTag, blank=True, related_name="posts", verbose_name="Teglar")

    reading_time_minutes = models.PositiveIntegerField(
        default=1, verbose_name="Taxminiy o'qish vaqti (daqiqa)"
    )
    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")

    is_published = models.BooleanField(default=True, verbose_name="Nashr etilganmi?")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Nashr etilgan vaqt")

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # O'qish vaqtini avtomatik hisoblash (o'rtacha daqiqada 180-200 so'z)
        if self.content:
            word_count = len(self.content.split())
            self.reading_time_minutes = max(1, math.ceil(word_count / 180))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def get_content_html(self):
        """
        Markdown matnni xavfsiz HTML va Pygments ranglangan kod bloklariga aylantirish.
        """
        raw_html = markdown.markdown(
            self.content,
            extensions=[
                "markdown.extensions.extra",
                "markdown.extensions.codehilite",
                "markdown.extensions.toc",
                "markdown.extensions.tables",
                "markdown.extensions.fenced_code",
            ],
        )
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
                "sub",
                "sup",
            ]
        )
        allowed_attrs = {
            "*": ["class", "id"],
            "a": ["href", "title", "target", "rel"],
            "img": ["src", "alt", "title"],
        }
        return bleach.clean(raw_html, tags=allowed_tags, attributes=allowed_attrs)
