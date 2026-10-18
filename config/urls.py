"""
URL configuration for rahmatullayev-uz project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.common.sitemaps import BlogSitemap, ProjectSitemap, StaticViewSitemap
from apps.common.views import robots_txt_view

sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
    "blog": BlogSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
    path("projects/", include("apps.projects.urls")),
    path("blog/", include("apps.blog.urls")),
    path("contact/", include("apps.contact.urls")),
    # SEO
    path(
        "sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"
    ),
    path("robots.txt", robots_txt_view, name="robots_txt"),
]

# Development rejimida media va statik fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin panel sarlavhalari
admin.site.site_header = "Rahmatullayev.uz Boshqaruv Paneli"
admin.site.site_title = "Rahmatullayev.uz Admin"
admin.site.index_title = "Boshqaruv Tizimi"
