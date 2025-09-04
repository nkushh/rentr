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

	def __str__(self):
		return f"{self.name} - {self.property.name}"
	
class Tenant(BaseModel):
	tenant_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	gender = models.CharField(max_length=255, null=True, blank=True)
	id_no = models.CharField(max_length=255)
	phone_no = models.CharField(max_length=255)
	email = models.CharField(max_length=255, null=True, blank=True)
	occupation = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return f"{self.name} - {self.id_no}"
	
class PropertyLease(BaseModel):
	property_unit = models.ForeignKey(PropertyUnit, null=True, on_delete=models.SET_NULL)
	tenant = models.ForeignKey(Tenant, null=True, on_delete=models.SET_NULL)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return f"{self.tenant.name} - {self.property_unit.name} - {self.property_unit.property.name}"


