from django.contrib import admin
from user.models import Biodata

# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat', 'telepon']
    search_fields = ['user_username']
admin.site.register(Biodata, BiodataAdmin)