from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import BlogPost
from apps.projects.models import Project


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["pages:home", "pages:about", "projects:list", "blog:list", "contact:contact"]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return Project.objects.all()

    def location(self, item):
        return reverse("projects:detail", kwargs={"slug": item.slug})

    def lastmod(self, item):
        return item.updated_at


class BlogSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def location(self, item):
        return reverse("blog:detail", kwargs={"slug": item.slug})

    def lastmod(self, item):
        return item.updated_at
