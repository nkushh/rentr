from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models as rental_models
# Serializers
from system_admin import serializers as admin_serializers
	
class PropertySerializer(ModelSerializer):
	property_type_detail = admin_serializers.PropertyTypeSerializer(source='property_type', read_only=True)

	class Meta:
		model = rental_models.Property
		fields = ['id', 'name', 'property_type', 'property_type_detail', 'county', 'physical_location', 'date_created', 'active_status']

	def create(self, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		validated_data['county'] = validated_data['county'].upper()
		validated_data['physical_location'] = validated_data['physical_location'].upper()

		return super().create(validated_data)

	def update(self, instance, validated_data):
		if 'name' in validated_data:
			validated_data['name'] = validated_data['name'].upper()
			validated_data['county'] = validated_data['county'].upper()
			validated_data['physical_location'] = validated_data['physical_location'].upper()

		return super().update(instance, validated_data)
	
class PropertyUnitSerializer(ModelSerializer):
	property_detail = PropertySerializer(source='property', read_only=True)
	class Meta:
		model = rental_models.PropertyUnit
		fields = ['id', 'property', 'property_detail', 'name', 'rent_amount', 'floor_area', 'bedrooms', 'vacant_status', 'date_created', 'active_status']

	def create(self, validated_data):
		validated_data['name'] = validated_data['name'].upper()

		if rental_models.PropertyUnit.objects.filter(property=validated_data['property'], name=validated_data['name']).exists():
			raise ValidationError("Property unit with provided details already exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()

		if rental_models.PropertyUnit.objects.filter(property=instance.property, name=validated_data['name']).exclude(pk=instance.pk).exists():
			raise ValidationError("Property unit with provided details already exists")
		return super().update(instance, validated_data)
	
class TenantsSerializer(ModelSerializer):
	class Meta:
		model = rental_models.Tenant
		fields = '__all__'

	def create(self, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		validated_data['id_no'] = validated_data['id_no'].upper()

		if 'email' in validated_data:
			validated_data['email'] = validated_data['email'].upper()
		if 'occupation' in validated_data:
			validated_data['occupation'] = validated_data['occupation'].upper()

		if rental_models.Tenant.objects.filter(id_no=validated_data['id_no']).exists():
			raise ValidationError("Tenant with similar details already exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		validated_data['id_no'] = validated_data['id_no'].upper()

		if 'email' in validated_data:
			validated_data['email'] = validated_data['email'].upper()
		if 'occupation' in validated_data:
			validated_data['occupation'] = validated_data['occupation'].upper()

		if rental_models.Tenant.objects.filter(id_no=validated_data['id_no']).exclude(pk=instance.pk).exists():
			raise ValidationError("Tenant with similar details already exists")
		return super().update(instance, validated_data)
		
		
