from django.contrib import admin
from .models import TopBanner, TopPacks, Careers
from .permission import TopBannerAdmin
from  django.contrib.auth.models  import  Group



@admin.register(TopBanner)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]


# admin.site.register(TopBanner, TopBannerAdmin)
#

admin.site.register(TopPacks)
admin.site.register(Careers)


admin.site.site_header = "MobStudio"
admin.site.site_title  =  "Custom bookstore admin site"
admin.site.index_title  =  "Custom Bookstore Admin"

admin.site.unregister(Group)  # new
