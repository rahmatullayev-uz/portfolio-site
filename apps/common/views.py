from django.http import HttpResponse


def robots_txt_view(request):
    """
    Qidiruv tizimlari botlari uchun robots.txt kontenti.
    """
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
