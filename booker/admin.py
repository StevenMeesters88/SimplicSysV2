from django.contrib import admin
from . import models


@admin.register(models.CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['regnr', 'first_name', 'last_name', 'telefon', 'email']
    search_fields = ['regnr', 'first_name', 'last_name', 'telefon', 'email']


@admin.register(models.ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['regnr', 'service_type', 'status', 'service_date', 'service_protocol_available']
    list_editable = ['status']


@admin.register(models.ServiceTypeModel)
class ServiceTypeModelAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price', 'visa_hemsida']
    list_editable = ['service_price', 'visa_hemsida']
    search_fields = ['service_name']


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['inkommen', 'regnr', 'klart']
    list_editable = ['klart']
    search_fields = ['regnr', 'telnr', 'email']


@admin.register(models.PaymentsModel)
class PaymentsModelAdmin(admin.ModelAdmin):
    list_display = ['regnr', 'service_date', 'betalstatus']
    search_fields = ['regnr']
