
from django.db import models

class SiteHeader(models.Model):
    logo_path = models.CharField(max_length=255, default='images/logo-dark.png')
    nav_home = models.CharField(max_length=50, default='Home')
    nav_about = models.CharField(max_length=50, default='About Us')
    nav_services = models.CharField(max_length=50, default='Services')
    nav_gallery = models.CharField(max_length=50, default='Gallery')
    nav_contact = models.CharField(max_length=50, default='Contact Us')
    header_button_text = models.CharField(max_length=50, blank=True, null=True)
    header_button_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Site Header"

class Hero(models.Model):
    title = models.TextField(blank=True)
    subtitle = models.TextField(blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.CharField(max_length=255, blank=True)
    image_path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Hero"

class About(models.Model):
    small_title = models.CharField(max_length=100, default='ABOUT US')
    heading = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image_path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "About"

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image_path = models.CharField(max_length=255, blank=True)
    icon_path = models.CharField(max_length=255, blank=True)
    readmore_url = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon_path = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class WhyChooseItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon_path = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Footer(models.Model):
    about_text = models.TextField(blank=True)
    quick_links = models.TextField(blank=True, help_text="Label|url per line")
    services_links = models.TextField(blank=True, help_text="Label|url per line")
    contact_email = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=100, blank=True)
    contact_address = models.TextField(blank=True)
    copyright_text = models.CharField(max_length=255, blank=True, default='© 2025 AKS. All Rights Reserved.')

    def __str__(self):
        return "Footer"
    



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

