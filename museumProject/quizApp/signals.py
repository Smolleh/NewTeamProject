from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserAchievements

#signal to create UserAchievements when a user is created
@receiver(post_save, sender=User)
def create_user_achievements(sender, instance, created, **kwargs):
    if created:
        UserAchievements.objects.get_or_create(user=instance)