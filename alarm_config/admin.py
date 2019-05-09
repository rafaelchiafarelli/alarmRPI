from django.contrib import admin
from .models import landpage
from landpage.models import Device
# Register your models here.
admin.site.register(landpage)
admin.site.register(Device)