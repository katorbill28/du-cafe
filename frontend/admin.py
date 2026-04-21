from django.contrib import admin
from .models import Cafe

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'campus', 'price_range')
    list_filter = ('campus',)
    search_fields = ('name', 'description')
