from django.shortcuts import render

from .models import Experience, Profile, Skill


def get_default_profile():
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            full_name="Sardor Rahmatullayev",
            title="Senior Python / Backend Muhandis",
            short_bio="Yuqori unumdorlikka ega backend tizimlar, mikroservislar va zamonaviy veb-arxitekturalar yaratish bo'yicha mutaxassis.",
            about_text="Men Python, Django, FastAPI, PostgreSQL va Docker texnologiyalarida yuqori yuklamali tizimlarni loyihalash va ishlab chiqish bo'yicha ko'p yillik tajribaga egaman.",
            email="rahmatullayev207@gmail.com",
            telegram_url="https://t.me/rahmatullayev_uz",
            github_url="https://github.com/rahmatullayev",
            linkedin_url="https://linkedin.com/in/rahmatullayev",
            years_of_experience=4,
            is_available_for_hire=True,
        )
    return profile


def home_view(request):
    profile = get_default_profile()
    skills = Skill.objects.all()[:8]

    # Kelgusi bosqichdagi loyihalar va maqolalarni chaqirishga tayyorgarlik
    featured_projects = []
    recent_posts = []
    try:
        from apps.projects.models import Project

        featured_projects = Project.objects.filter(is_featured=True)[:3]
    except Exception:
        pass

    try:
        from apps.blog.models import BlogPost

        recent_posts = BlogPost.objects.filter(is_published=True)[:3]
    except Exception:
        pass

    context = {
        "profile": profile,
        "skills": skills,
        "featured_projects": featured_projects,
        "recent_posts": recent_posts,
    }
    return render(request, "pages/home.html", context)


def about_view(request):
    profile = get_default_profile()

    # Ko'nikmalarni kategoriyalar bo'yicha guruhlash
    backend_skills = Skill.objects.filter(category=Skill.Category.BACKEND)
    database_skills = Skill.objects.filter(category=Skill.Category.DATABASE)
    devops_skills = Skill.objects.filter(category=Skill.Category.DEVOPS)
    tool_skills = Skill.objects.filter(category=Skill.Category.TOOLS)

    experiences = Experience.objects.all()

    context = {
        "profile": profile,
        "backend_skills": backend_skills,
        "database_skills": database_skills,
        "devops_skills": devops_skills,
        "tool_skills": tool_skills,
        "experiences": experiences,
    }
    return render(request, "pages/about.html", context)
