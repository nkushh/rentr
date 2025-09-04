from django.contrib import admin
from . import models as admin_models

# Register your models here.
admin.site.register(admin_models.PropertyCategory)
admin.site.register(admin_models.PropertyDepositCategory)
admin.site.register(admin_models.PropertyReccurentPayment)
admin.site.register(admin_models.PropertyType)
