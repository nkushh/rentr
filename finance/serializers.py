from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from . import models as finance_models

class PropertyLeaseChargesSerializer(ModelSerializer):
	class Meta:
		model = finance_models.PropertyLeaseCharge
		fields = '__all__'

	def create(self, validated_data):
		if finance_models.PropertyLeaseCharge.objects.filter(property=validated_data['property'], charge=validated_data['charge']).exists():
			raise ValidationError("A record with similar details already exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		if finance_models.PropertyLeaseCharge.objects.filter(property=validated_data['property'], charge=validated_data['charge']).exclude(pk=instance.pk).exists():
			raise ValidationError("A record with similar details already exists")
		return super().update(instance, validated_data)
	
class PropertyRecurrentChargesSerializer(ModelSerializer):
	class Meta:
		model = finance_models.PropertyRecurrentCharge
		fields = '__all__'

	def create(self, validated_data):
		if finance_models.PropertyRecurrentCharge.objects.filter(property=validated_data['property'], charge=validated_data['charge']).exists():
			raise ValidationError("A record with similar details already exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		if finance_models.PropertyRecurrentCharge.objects.filter(property=validated_data['property'], charge=validated_data['charge']).exclude(pk=instance.pk).exists():
			raise ValidationError("A record with similar details already exists")
		return super().update(instance, validated_data)