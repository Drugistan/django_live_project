from django.contrib import admin, messages
from .models import TopBanner, CareerBanner, AboutBanner


class CareerBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(CareerBanner.objects.select_related().all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if obj:
            self.message_user(request, "Permissions, Change Now You Can Only Update Career Banner",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False


class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(AboutBanner.objects.select_related().all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if obj:
            self.message_user(request, "Permissions, Change Now You Can Only Update About Banner",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False


class CustomTopBanner(admin.ModelAdmin):
    list_display = ["title", "description"]

    def has_add_permission(self, request):
        if len(TopBanner.objects.all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if obj:
            self.message_user(request, "Permissions, Change Now You Can Only Update Top Banner",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False
