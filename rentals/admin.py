from django.contrib import admin
from . import models as rental_models

# Register your models here.
admin.site.register(rental_models.Property)
admin.site.register(rental_models.PropertyCategory)
admin.site.register(rental_models.PropertyLease)
admin.site.register(rental_models.PropertyType)
admin.site.register(rental_models.PropertyUnit)
admin.site.register(rental_models.Tenant)
