from django.core.paginator import Paginator
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, render

from .models import BlogCategory, BlogPost, BlogTag


def blog_list_view(request):
    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "").strip()
    tag_slug = request.GET.get("tag", "").strip()

    posts = (
        BlogPost.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related("tags")
    )

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query)
        )

    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    # Sahifalash (har bir sahifada 6 ta maqola)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    categories = BlogCategory.objects.all()
    popular_tags = BlogTag.objects.all()[:15]

    context = {
        "page_obj": page_obj,
        "posts": page_obj.object_list,
        "categories": categories,
        "popular_tags": popular_tags,
        "query": query,
        "active_category": category_slug,
        "active_tag": tag_slug,
    }

    if request.headers.get("HX-Request"):
        return render(request, "blog/partials/post_list.html", context)

    return render(request, "blog/list.html", context)


def blog_detail_view(request, slug):
    post = get_object_or_404(
        BlogPost.objects.select_related("category").prefetch_related("tags"),
        slug=slug,
        is_published=True,
    )

    # Ko'rishlar sonini xavfsiz oshirish
    BlogPost.objects.filter(id=post.id).update(views_count=F("views_count") + 1)
    post.refresh_from_db(fields=["views_count"])

    # O'xshash maqolalar (kategoriya bo'yicha)
    related_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id)
    if post.category:
        related_posts = related_posts.filter(category=post.category)[:2]
    else:
        related_posts = related_posts[:2]

    context = {
        "post": post,
        "related_posts": related_posts,
    }
    return render(request, "blog/detail.html", context)
