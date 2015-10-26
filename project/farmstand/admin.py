from django.contrib import admin
from farmstand.models import Products, Season, Week, UserProfile
# Register your models here.

admin.site.register(Products)
admin.site.register(UserProfile)
admin.site.register(Season)
admin.site.register(Week)