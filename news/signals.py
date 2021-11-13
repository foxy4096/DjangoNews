from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from django.contrib.auth.models import User

from .models import Article

content_type = ContentType.objects.get_for_model(Article)
permission = Permission.objects.filter(content_type=content_type)

@receiver(post_save, sender=User)
def set_staff(sender, created, instance, **kwargs):
    if created:
        instance.is_staff = True
        instance.user_permissions.set(permission)
        instance.save()
