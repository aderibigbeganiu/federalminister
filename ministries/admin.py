from django.contrib import admin
from .models import Ministries

class MinistriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Ministries, MinistriesAdmin)
