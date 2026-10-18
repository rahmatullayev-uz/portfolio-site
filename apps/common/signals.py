import logging

from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from apps.blog.models import BlogPost
from apps.pages.models import Experience, Profile, Skill
from apps.projects.models import Project

logger = logging.getLogger(__name__)


@receiver([post_save, post_delete], sender=Project)
@receiver([post_save, post_delete], sender=BlogPost)
@receiver([post_save, post_delete], sender=Profile)
@receiver([post_save, post_delete], sender=Skill)
@receiver([post_save, post_delete], sender=Experience)
def clear_site_cache(sender, instance, **kwargs):
    """
    Ma'lumotlar o'zgarganda (yangi post, yangi loyiha yoki tahrirlashda)
    tegishli Redis keshlarini tozalash.
    """
    try:
        cache.clear()
        logger.info(f"Kesh muvaffaqiyatli tozalandi: {sender.__name__} o'zgardi.")
    except Exception as exc:
        logger.warning(f"Keshni tozalashda xatolik: {exc}")
