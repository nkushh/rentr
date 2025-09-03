from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models as rental_models

class PropertyCategorySerializer(ModelSerializer):
	class Meta:
		model = rental_models.PropertyCategory
		fields = '__all__'

	def create(self, validated_data):
		name = validated_data.get('name').upper()

		validated_data['name'] = name
		if rental_models.PropertyCategory.objects.filter(name=name).exists():
			raise ValidationError("A property category with similar details exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		name = validated_data['name']

		if rental_models.PropertyCategory.objects.filter(name=name).exclude(pk=instance.pk).exists():
			raise ValidationError("A property category with similar details exists")
		return super().update(instance, validated_data)

class PropertyTypeSerializer(ModelSerializer):
	property_category_detail = PropertyCategorySerializer(source='property_category', read_only=True)

	class Meta:
		model = rental_models.PropertyType
		fields = ['id', 'name', 'property_category', 'property_category_detail', 'date_created', 'active_status']

	def create(self, validated_data):
		name = validated_data.get('name').upper()
		property_category = validated_data.get('property_category', None)

		validated_data['name'] = name
		validated_data['property_category'] = property_category
		
		if rental_models.PropertyType.objects.filter(name=name).exists():
			raise ValidationError("Another property type with a similar details exists") 
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		if 'name' in validated_data:
			validated_data['name'] = validated_data['name'].upper()

			name = validated_data['name']
			if rental_models.PropertyType.objects.filter(name=name).exclude(pk=instance.pk).exists():
				raise ValidationError("A property type with this name already exists.")

		return super().update(instance, validated_data)
	
class PropertySerializer(ModelSerializer):
	property_type_detail = PropertyTypeSerializer(source='property_type', read_only=True)

	class Meta:
		model = rental_models.Property
		fields = ['id', 'name', 'property_type', 'property_type_detail', 'county', 'physical_location', 'date_created', 'active_status']

	def create(self, validated_data):
		name = validated_data.get('name').upper()
		property_type = validated_data.get('property_type', None)
		county = validated_data.get('county').upper()
		physical_location = validated_data.get('physical_location').upper()

		validated_data['name'] = name
		validated_data['property_type'] = property_type
		validated_data['county'] = county
		validated_data['physical_location'] = physical_location

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
		property = validated_data.get('property', None)
		name = validated_data.get('name').upper()

		validated_data['name'] = name
		if rental_models.PropertyUnit.objects.filter(property=property, name=name).exists():
			raise ValidationError("Property unit with provided details already exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		validated_data['property'] = instance.property
		
		if rental_models.PropertyUnit.objects.filter(property=instance.property, name=validated_data['name']).exclude(pk=instance.pk).exists():
			raise ValidationError("Property unit with provided details already exists")
		return super().update(instance, validated_data)
		
