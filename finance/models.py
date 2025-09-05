from django.db import models
from system_admin.models import BaseModel

# Create your models here.
class PropertyLeaseCharge(BaseModel):
	property = models.ForeignKey('rentals.Property', null=True, on_delete=models.SET_NULL)
	charge = models.ForeignKey('system_admin.PropertyDepositCategory', null=True, on_delete=models.SET_NULL)
	amount = models.DecimalField(max_digits=12, decimal_places=2)

	def __str__(self):
		return f"{self.charge.name} - {self.property.name}" # type: ignore
	
class PropertyRecurrentCharge(BaseModel):
	property = models.ForeignKey('rentals.Property', null=True, on_delete=models.SET_NULL)
	charge = models.ForeignKey('system_admin.PropertyReccurentPayment', null=True, on_delete=models.SET_NULL)
	amount = models.DecimalField(max_digits=12, decimal_places=2)

	def __str__(self):
		return f"{self.charge.name} - {self.property.name}" # type: ignore
