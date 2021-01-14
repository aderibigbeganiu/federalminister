from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Ministries

class MinistriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'minister')

admin.site.register(Ministries, MinistriesAdmin)
