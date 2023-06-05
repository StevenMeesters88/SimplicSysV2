from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.


class StandardOffertInline(admin.TabularInline):
    model = models.OffertPost


@admin.register(models.StandardOffert)
class StandardOffertAdmin(admin.ModelAdmin):
    list_display = ['offert', 'regnr', 'totalpris']
    search_fields = ['regnr__icontains']
    inlines = [StandardOffertInline]
