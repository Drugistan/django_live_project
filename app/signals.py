from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import *


# @receiver(pre_save, sender=TopBanner)
# def update_previous_active(sender, instance, **kwargs):
#     if instance.is_active:
#         TopBanner.active_banners.get_active_banner().exclude(pk=instance.pk).update(is_active=False)
#


@receiver(post_delete)
def delete_file_on_post_delete(sender, instance, **kwargs):
    if hasattr(instance, 'image'):
        instance.image.delete(False)


@receiver(post_delete, sender=TopPacks)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=TopBanner)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=TopPacks)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=Careers)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=CareerBanner)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=AboutBanner)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=PortFolio)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=AboutAsserts)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)


@receiver(post_delete, sender=WhyChoseUs)
def delete_file_on_top_packs(sender, instance, **kwargs):
    delete_file_on_post_delete(sender, instance, **kwargs)
