from django.db import models

# Create your models here.
class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	active_status = models.BooleanField(default=True)

	class Meta:
		abstract = True
