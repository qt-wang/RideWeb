"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import driver


@receiver(post_save, sender=User)
def create_driver(sender, instance, created, **kwargs):
    if created:
        driver.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_driver(sender, instance, **kwargs):
    instance.driver.save()
    """