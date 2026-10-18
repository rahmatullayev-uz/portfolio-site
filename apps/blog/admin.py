from django.contrib import admin

from .models import BlogCategory, BlogPost, BlogTag


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "reading_time_minutes",
        "views_count",
        "is_published",
        "published_at",
    )
    list_filter = ("is_published", "category", "tags", "published_at")
    list_editable = ("is_published",)
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    date_hierarchy = "published_at"
    fieldsets = (
        ("Asosiy Ma'lumotlar", {"fields": ("title", "slug", "category", "cover_image", "summary")}),
        ("Maqola Matni (Markdown)", {"fields": ("content",)}),
        ("Teglar va Nashr Holati", {"fields": ("tags", "is_published", "published_at")}),
        (
            "Statistika",
            {
                "fields": ("reading_time_minutes", "views_count"),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("reading_time_minutes", "views_count")
