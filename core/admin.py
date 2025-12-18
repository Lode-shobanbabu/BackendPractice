from django.contrib import admin
from .models import SiteHeader, Hero, About, Service, Feature, WhyChooseItem, Footer

@admin.register(SiteHeader)
class SiteHeaderAdmin(admin.ModelAdmin):
    list_display = ('logo_path', 'header_button_text')

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('small_title', 'heading')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(WhyChooseItem)
class WhyChooseItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('contact_email', 'contact_phone')



from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
