from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    extra = 0


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
    raw_id_fields = ["how_much_like"]
    inlines = [FlatOwnersInline]

admin.site.register(Complaint)
admin.site.register(Flat, HausAdmin)
admin.site.register(Owner)
