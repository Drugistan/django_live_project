from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import TopBanner


# @receiver(pre_save, sender=TopBanner)
# def update_previous_active(sender, instance, **kwargs):
#     if instance.is_active:
#         TopBanner.active_banners.get_active_banner().exclude(pk=instance.pk).update(is_active=False)
#

