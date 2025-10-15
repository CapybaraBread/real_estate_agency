from django.contrib import admin

from .models import Flat

class HausAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'price')
admin.site.register(Flat, HausAdmin)
