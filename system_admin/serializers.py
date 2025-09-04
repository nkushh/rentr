from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models as admin_models

class PropertyCategorySerializer(ModelSerializer):
	class Meta:
		model = admin_models.PropertyCategory
		fields = '__all__'

	def create(self, validated_data):
		validated_data['name'] = validated_data.get('name').upper()

		if admin_models.PropertyCategory.objects.filter(name=validated_data['name']).exists():
			raise ValidationError("A property category with similar details exists")
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()

		if admin_models.PropertyCategory.objects.filter(name=validated_data['name']).exclude(pk=instance.pk).exists():
			raise ValidationError("A property category with similar details exists")
		return super().update(instance, validated_data)

class PropertyTypeSerializer(ModelSerializer):
	property_category_detail = PropertyCategorySerializer(source='property_category', read_only=True)

	class Meta:
		model = admin_models.PropertyType
		fields = ['id', 'name', 'property_category', 'property_category_detail', 'date_created', 'active_status']

	def create(self, validated_data):
		validated_data['name'] = validated_data['name'].upper()
		
		if admin_models.PropertyType.objects.filter(name=validated_data['name']).exists():
			raise ValidationError("Another property type with a similar details exists") 
		return super().create(validated_data)
	
	def update(self, instance, validated_data):
		validated_data['name'] = validated_data['name'].upper()

		if admin_models.PropertyType.objects.filter(name=validated_data['name']).exclude(pk=instance.pk).exists():
			raise ValidationError("A property type with this name already exists.")
		return super().update(instance, validated_data)