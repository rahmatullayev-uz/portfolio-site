from django.shortcuts import get_object_or_404, render

from .models import Project, ProjectCategory, Technology


def project_list_view(request):
    category_slug = request.GET.get("category", "").strip()
    tech_slug = request.GET.get("tech", "").strip()

    projects = Project.objects.select_related("category").prefetch_related("technologies").all()

    if category_slug:
        projects = projects.filter(category__slug=category_slug)

    if tech_slug:
        projects = projects.filter(technologies__slug=tech_slug)

    categories = ProjectCategory.objects.all()
    technologies = Technology.objects.all()

    context = {
        "projects": projects,
        "categories": categories,
        "technologies": technologies,
        "active_category": category_slug,
        "active_tech": tech_slug,
    }

    # Agar so'rov HTMX orqali kelgan bo'lsa, faqat grid qismini qaytarish
    if request.headers.get("HX-Request"):
        return render(request, "projects/partials/project_grid.html", context)

    return render(request, "projects/list.html", context)


def project_detail_view(request, slug):
    project = get_object_or_404(
        Project.objects.select_related("category").prefetch_related("technologies"), slug=slug
    )

    # O'xshash loyihalar
    related_projects = Project.objects.exclude(id=project.id)
    if project.category:
        related_projects = related_projects.filter(category=project.category)[:2]
    else:
        related_projects = related_projects[:2]

    context = {
        "project": project,
        "related_projects": related_projects,
    }
    return render(request, "projects/detail.html", context)
