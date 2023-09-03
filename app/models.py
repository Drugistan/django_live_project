from django.db import models
import os

from app.managers import ActiveCareersManager, ActiveTopPacksManager, ActiveTestimonialsManager, ActiveFAQManager, \
    PortFolioQManager


def image_path_rename(instance, filename):
    upload_to = instance.folder_name
    return os.path.join(upload_to, filename)


class TopBanner(models.Model):
    objects = None
    folder_name = "TopBannerImages"
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False, default="")
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Top Banner"


class TopPacks(models.Model):
    image_by_title = models.CharField(max_length=100, null=False, blank=False)
    folder_name = "TopPacks"
    add_image = models.ImageField(upload_to=image_path_rename, max_length=255, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    get_active_packs = ActiveTopPacksManager()

    def __str__(self):
        return "Image add by this name {} ".format(self.add_image)

    class Meta:
        verbose_name_plural = "Top Packs"


class Testimonial(models.Model):
    objects = None
    client_name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=100, null=False, blank=False)
    company = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    active_testimonial = ActiveTestimonialsManager()

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = "Testimonial"


class Careers(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=True, blank=True)
    job_role = models.TextField()
    folder_name = "Careers"
    image = models.ImageField(upload_to=image_path_rename, null=True, blank=True)
    is_full_time_role = models.BooleanField(default=False)
    is_remote_role = models.BooleanField(default=False)
    created_at = models.DateField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=False)
    active_career = ActiveCareersManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Careers"


class CareerBanner(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    folder_name = "CareerBanner"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False, default="")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Career Banner"


class AboutBanner(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    folder_name = "AboutBanner"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Banner"


class FAQ(models.Model):
    question = models.CharField(max_length=200, null=False, blank=False)
    answer = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=False)
    active_faq = ActiveFAQManager()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQ"


class PortFolio(models.Model):
    folder_name = "Porfolio"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)
    portfolio_detail = models.TextField(null=True, blank=True)
    portfolio_title = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    active_portfolio = PortFolioQManager()

    def __str__(self):
        return self.portfolio_title

    class Meta:
        verbose_name_plural = "Portfolio"


class AboutAsserts(models.Model):
    objects = None
    folder_name = "Asserts"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)
    assert_detail = models.TextField(null=True, blank=True)
    assert_title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.assert_title

    class Meta:
        verbose_name_plural = "About Asserts"


class WhyChoseUs(models.Model):
    objects = None
    folder_name = "WhyChoseUs"
    image = models.ImageField(upload_to=image_path_rename, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Why Chose Us"
