from django.contrib import admin

from .models import ContactUs, OurStaff, SiteSettings, Testimonial

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'title']

@admin.register(OurStaff)
class OurStaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fieldsets = (
        ('Site Header', {"fields": ('site_logo',) } ),
        
        ('Contact Info', {"fields": ('site_email', 'site_phone', 'site_cell', 'site_address', ) } ),
        
        ('About Us', {"fields": ('site_story_short', 'site_story_long') } ),
        
        )
    