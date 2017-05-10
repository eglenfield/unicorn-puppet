from django.contrib import admin

# Register your models here.

from .models import Packages, Users, Volumes

admin.site.register(Packages)
admin.site.register(Users)
admin.site.register(Volumes)