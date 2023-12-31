from django.db import models


class ActiveCareersManager(models.Manager):
    def get_active_career(self):
        return super().get_queryset().filter(is_active=True)


class ActiveTopPacksManager(models.Manager):
    def get_active_packs(self):
        return super().get_queryset().filter(is_active=True).order_by("-date_added")[:10]


class ActiveTestimonialsManager(models.Manager):
    def get_active_testimonial(self):
        return super().get_queryset().filter(is_active=True).order_by("-id")[:10]


class ActiveFAQManager(models.Manager):
    def get_active_faq(self):
        return super().get_queryset().filter(is_active=True).order_by("-id")


class ActiveEmailManager(models.Manager):
    def get_active_emails(self):
        return super().get_queryset().filter(is_active=True).order_by("-id")[:5]
