from django.db import models
from system_admin.models import BaseModel

# Create your models here.
class PropertyCategory(BaseModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class PropertyType(BaseModel):
	name = models.CharField(max_length=255)
	property_category = models.ForeignKey(PropertyCategory, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name
	
class Property(BaseModel):
	name = models.CharField(max_length=255)
	property_type = models.ForeignKey(PropertyType, null=True, on_delete=models.SET_NULL)
	county = models.CharField(max_length=255)
	physical_location = models.CharField(max_length=255)

	def __str__(self):
		return self.name
	
class PropertyUnit(BaseModel):
	property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=255)
	rent_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
	floor_area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	bedrooms = models.PositiveIntegerField(null=True, blank=True)
	vacant_status = models.BooleanField(default=True)
