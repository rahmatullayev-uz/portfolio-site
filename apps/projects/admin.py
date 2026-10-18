from django.contrib import admin

from .models import Project, ProjectCategory, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "badge_color")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "sort_order", "created_at")
    list_filter = ("category", "is_featured", "technologies")
    list_editable = ("is_featured", "sort_order")
    search_fields = ("title", "short_description", "full_description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    fieldsets = (
        (
            "Asosiy Ma'lumotlar",
            {"fields": ("title", "slug", "category", "cover_image", "short_description")},
        ),
        ("Batafsil Tavsif (Markdown)", {"fields": ("full_description",)}),
        (
            "Texnologiyalar va Havolalar",
            {"fields": ("technologies", "github_url", "live_demo_url")},
        ),
        ("Boshqaruv Sozlamalari", {"fields": ("is_featured", "sort_order")}),
    )
