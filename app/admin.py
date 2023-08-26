from django.contrib import admin, messages
from rest_framework.exceptions import ValidationError

from .models import TopBanner, TopPacks, Careers, Testimonial, CareerBanner, AboutBanner, TopBannerImages
from .permission import CustomAdmin, CustomTopBanner
from django.contrib.auth.models import Group

# @admin.register(TopBanner)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ["title", "description", "image"]


admin.site.register(TopBanner, CustomTopBanner)
admin.site.register(CareerBanner, CustomAdmin)
admin.site.register(AboutBanner)
admin.site.register(TopBannerImages)


class TopPacksModelAdmin(admin.ModelAdmin):
    list_display = ['add_image', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Warning: 'is_active' field is not checked. Otherwise new data will not show",
                              level=messages.WARNING)
        super().save_model(request, obj, form, change)


admin.site.register(TopPacks, TopPacksModelAdmin)


class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'designation', 'company', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Warning: 'is_active' field is not checked. Otherwise new data will not show",
                              level=messages.WARNING)
            self.message_user(request, "Warning: at least one Testimonial must be marks ad check 'is_active' ",
                              level=messages.WARNING)
        super().save_model(request, obj, form, change)


admin.site.register(Testimonial, TestimonialModelAdmin)


class CareersModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_role', 'is_full_time_role', 'is_remote_role', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Warning: 'is_active' field is not checked. Otherwise new data will not show",
                              level=messages.WARNING)
            self.message_user(request, "Warning: at least one Career must be marks ad check 'is_active' ",
                              level=messages.WARNING)
        super().save_model(request, obj, form, change)


admin.site.register(Careers, CareersModelAdmin)

admin.site.site_header = "Mob Studios"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Features"

admin.site.unregister(Group)  # new
