from django.db import models

# Create your models here.
class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	active_status = models.BooleanField(default=True)

	class Meta:
		abstract = True

class PropertyCategory(BaseModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class PropertyType(BaseModel):
	name = models.CharField(max_length=255)
	property_category = models.ForeignKey(PropertyCategory, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name
	
class PropertyDepositCategory(BaseModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name
	
class PropertyReccurentPayment(BaseModel):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name