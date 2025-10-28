from django.contrib import admin

from .models import Flat


class HausAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'price', 'owner')
    readonly_fields = ['created_at']


admin.site.register(Flat, HausAdmin)

