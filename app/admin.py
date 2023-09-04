from django.contrib import admin, messages

from .models import TopBanner, TopPacks, Careers, Testimonial, CareerBanner, AboutBanner, FAQ, PortFolio, AboutAsserts, \
    WhyChoseUs
from .permission import CareerBannerAdmin, CustomTopBanner, AboutBannerAdmin
from django.contrib.auth.models import Group

admin.site.register(TopBanner, CustomTopBanner)
admin.site.register(CareerBanner, CareerBannerAdmin)
admin.site.register(AboutBanner, AboutBannerAdmin)


class TopPacksModelAdmin(admin.ModelAdmin):
    list_display = ['image_by_title', 'add_image', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Reminder. You are added something new."
                                       " But you are not checked ' is_active ' option",
                              level=messages.WARNING)
            self.message_user(request, "At Least one or more then one Top Packs must be ' is_active ' "
                                       "checked otherwise new data will not appear on screen",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)


admin.site.register(TopPacks, TopPacksModelAdmin)


class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'designation', 'company', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Reminder. You are added something new."
                                       "But you are not checked ' is_active ' option",
                              level=messages.WARNING)
            self.message_user(request, "At Least one or more then one Testimonials must be ' is_active ' "
                                       "checked otherwise new data will not appear on screen",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)


admin.site.register(Testimonial, TestimonialModelAdmin)


class CareersModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_role', 'is_full_time_role', 'is_remote_role', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Reminder. You are added something new."
                                       "But you are not checked ' is_active ' option",
                              level=messages.WARNING)
            self.message_user(request, "At Least one or more then one Career must be ' is_active ' "
                                       "checked otherwise new data will not appear on screen",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)


admin.site.register(Careers, CareersModelAdmin)


class FAQModelAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_active']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Reminder. You are added something new."
                                       "But you are not checked ' is_active ' option",
                              level=messages.WARNING)
            self.message_user(request, "At Least one or more then one FAQS must be ' is_active ' "
                                       "checked otherwise new data will not appear on screen",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)


admin.site.register(FAQ, FAQModelAdmin)


class PortFolioModelAdmin(admin.ModelAdmin):
    list_display = ['portfolio_title', 'portfolio_detail', 'is_active', 'image']

    def save_model(self, request, obj, form, change):
        if not obj.is_active:
            self.message_user(request, "Reminder. You are added something new."
                                       "But you are not checked ' is_active ' option",
                              level=messages.WARNING)
            self.message_user(request, "At Least one or more then one Portfolio must be ' is_active ' "
                                       "checked otherwise new data will not appear on screen",
                              level=messages.INFO)
        super().save_model(request, obj, form, change)


admin.site.register(PortFolio, PortFolioModelAdmin)


class AboutAssertsModelAdmin(admin.ModelAdmin):
    list_display = ['assert_title', 'assert_detail', 'image']


admin.site.register(AboutAsserts, AboutAssertsModelAdmin)


class WhyChoseUsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


admin.site.register(WhyChoseUs, WhyChoseUsModelAdmin)

admin.site.site_header = "MOB STUDIO"
admin.site.site_title = "ADMIN CONTROL"
admin.site.index_title = "ADMINISTRATION FEATURES"

admin.site.unregister(Group)  # new
