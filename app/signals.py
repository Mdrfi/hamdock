from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from app.models import App, client


@receiver(post_delete, sender=App)
def app_post_delete(sender, instance, **kwargs):
    client.images.remove_container()


@receiver(post_save, sender=App)
def app_post_save(sender, instance, created, **kwargs):
    if not created:
        for container in instance.containers():
            container.reload()
