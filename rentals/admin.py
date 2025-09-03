from django.contrib import admin
from . import models as rental_models

# Register your models here.
admin.site.register(rental_models.Property)
admin.site.register(rental_models.PropertyType)
admin.site.register(rental_models.PropertyUnit)
