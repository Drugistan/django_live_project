from django.contrib import admin, messages
from .models import TopBanner, CareerBanner, AboutBanner, ContactBanner, WhyChoseUs


class CareerBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(CareerBanner.objects.select_related().all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        try:
            original_obj = CareerBanner.objects.get(pk=obj.pk)
            if original_obj:
                pass
        except:
            if obj:
                self.message_user(request, "Permissions, Change Now You Can Only Update Career Banner",
                                  level=messages.INFO)
            super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return True


class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(AboutBanner.objects.select_related().all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        try:
            original_obj = AboutBanner.objects.get(pk=obj.pk)
            if original_obj:
                pass
        except:
            if obj:
                self.message_user(request, "Permissions, Change Now You Can Only Update About Banner",
                                  level=messages.INFO)
            super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return True


class CustomTopBanner(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(TopBanner.objects.all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        try:
            original_obj = TopBanner.objects.get(pk=obj.pk)
            if original_obj:
                pass
        except:
            if obj:
                self.message_user(request, "Permissions, Change Now You Can Only Update Top Banner",
                                  level=messages.INFO)
            super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return True


class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

    def has_add_permission(self, request):
        if len(ContactBanner.objects.all()) > 0:
            return False
        return True

    def save_model(self, request, obj, form, change):
        try:
            original_obj = CareerBanner.objects.get(pk=obj.pk)
            if original_obj:
                pass
        except:
            if obj:
                self.message_user(request, "Permissions, Change Now You Can Only Contact Banner",
                                  level=messages.INFO)
            super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return True


class WhyChoseUsAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    is_limit = False

    def has_add_permission(self, request):
        if len(WhyChoseUs.objects.all()) >= 6:
            self.is_limit = True
            return False
        return True

    def save_model(self, request, obj, form, change):
        if self.is_limit:
            self.message_user(request, "You are successfully added 6 items. Now you can only Update this items",
                              level=messages.WARNING)
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return True


