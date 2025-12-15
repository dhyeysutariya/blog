from django.contrib import admin

from assignments.models import About, SocialLink

class AboutAdmin(admin.ModelAdmin):
    list_display=('about_heading','about_description')

    def has_add_permission(self,request):
        count=About.objects.count()
        if count==0:
            return True
        return False

admin.site.register(About,AboutAdmin)

class SocialLinkAdmin(admin.ModelAdmin):
    list_display=('platform_name','account_url')

admin.site.register(SocialLink,SocialLinkAdmin)
