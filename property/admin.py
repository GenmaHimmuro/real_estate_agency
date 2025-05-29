from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town','address',]
    readonly_fields = ['created_at',]
    list_display = ['address', 'construction_year', 'price', 'town', 'new_building',]
    list_editable = ['new_building',]
    list_filter = ['new_building',]


admin.site.register(Flat, FlatAdmin)
