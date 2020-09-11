from django.contrib import admin
from authapp.models import ShopUser, ShopUserProfile

# Register your models here.

admin.site.register(ShopUser)
admin.site.register(ShopUserProfile)
