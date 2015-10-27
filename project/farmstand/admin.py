from django.contrib import admin
from farmstand.models import Product, Season, Week, Week_Product, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Season)
admin.site.register(Week)
admin.site.register(Product)
admin.site.register(Week_Product)