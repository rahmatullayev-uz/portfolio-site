from django.contrib import admin

from .models import Experience, Profile, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "is_available_for_hire")
    fieldsets = (
        (
            "Asosiy Ma'lumotlar",
            {
                "fields": (
                    "full_name",
                    "title",
                    "avatar",
                    "resume_file",
                    "years_of_experience",
                    "is_available_for_hire",
                )
            },
        ),
        ("Matnlar", {"fields": ("short_bio", "about_text")}),
        (
            "Aloqa va Ijtimoiy Tarmoqlar",
            {"fields": ("email", "telegram_url", "github_url", "linkedin_url")},
        ),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    list_editable = ("order", "proficiency")
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date", "is_current", "order")
    list_filter = ("is_current",)
    list_editable = ("order",)
    search_fields = ("position", "company", "description")
