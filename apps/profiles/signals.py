import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates user's profile when new user is created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """save profile when user instance saved"""
    instance.profile.save()
    logger.info(f"{instance}'s profile created")