from django.db import models
import os

from app.managers import ActiveCareersManager, ActiveTopPacksManager


def image_path_rename(instance, filename):
    upload_to = instance.folder_name
    return os.path.join(upload_to, filename)


class TopBanner(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    folder_name = "TopBanner"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)

    def __str__(self):
        return self.title


class TopPacks(models.Model):
    folder_name = "TopPacks"
    add_image = models.ImageField(upload_to=image_path_rename, max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    get_active_packs = ActiveTopPacksManager()

    def __str__(self):
        return "Image add by this name {} ".format(self.add_image)


class Testimonial(models.Model):
    objects = None
    client_name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=100, null=False, blank=False)
    company = models.CharField(max_length=100, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.client_name


class Careers(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=True, blank=True)
    job_role = models.TextField()
    folder_name = "Careers"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)
    is_full_time_role = models.BooleanField(default=False)
    is_remote_role = models.BooleanField(default=False)
    created_at = models.DateField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=False)
    active_career = ActiveCareersManager()

    def __str__(self):
        return self.title


class CareerBanner(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    folder_name = "CareerBanner"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False, default="")

    def __str__(self):
        return self.title
