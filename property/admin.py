from django.contrib import admin

from .models import Flat


class HausAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'price', 'owner')
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'town',
        'price',
        'construction_year',
        'new_building',
    )
    list_editable = ['new_building']
    list_filter = ['new_building']



admin.site.register(Flat, HausAdmin)

