from django.db.models import Count, Q
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
# Models
from . import models as rental_models
# Serializers
from . import serializers as rental_serializers

# Create your views here.
def property_categories(request):
	return render(request, 'rentals/property_categories.html')

class ListCreatePropertyCategory(ListCreateAPIView):
	queryset = rental_models.PropertyCategory.objects.order_by('name')
	serializer_class = rental_serializers.PropertyCategorySerializer

class PropertyCategoryDetail(RetrieveUpdateDestroyAPIView):
	queryset = rental_models.PropertyCategory.objects.order_by('name')
	serializer_class = rental_serializers.PropertyCategorySerializer
	lookup_field = 'pk'

def property_types(request):
	property_categories = rental_models.PropertyCategory.objects.order_by('name')
	context = {
		'property_categories' : property_categories
	}
	return render(request, 'rentals/property_types.html', context)

class ListCreatePropertyType(ListCreateAPIView):
    queryset = rental_models.PropertyType.objects.select_related('property_category').order_by('name')
    serializer_class = rental_serializers.PropertyTypeSerializer
    
class PropertyTypeDetail(RetrieveUpdateDestroyAPIView):
	queryset = rental_models.PropertyType.objects.select_related('property_category').order_by('name')
	serializer_class = rental_serializers.PropertyTypeSerializer
	lookup_field = 'pk'

def properties(request):
	property_types = rental_models.PropertyType.objects.order_by('name')
	context = {
		'property_types' : property_types
	}
	return render(request, 'rentals/properties.html', context)

class ListCreateProperty(ListCreateAPIView):
	queryset = rental_models.Property.objects.select_related('property_type__property_category').order_by('name')
	serializer_class = rental_serializers.PropertySerializer

class PropertyDetail(RetrieveUpdateDestroyAPIView):
	queryset = rental_models.Property.objects.order_by('name')
	serializer_class = rental_serializers.PropertySerializer
	lookup_field = 'pk'

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)

		units_queryset = rental_models.PropertyUnit.objects.filter(property=instance).order_by('name')
		units_serializer = rental_serializers.PropertyUnitSerializer(units_queryset, many=True)

		aggregates = units_queryset.aggregate(
			total_units=Count('pk'), 
			total_occupied=Count('pk', filter=Q(vacant_status=False)), 
			total_vacant=Count('pk', filter=Q(vacant_status=True))
		)

		data = {
			'property_details' : serializer.data,
			'units' : units_serializer.data,
			'property_aggregate' : aggregates
		}

		return Response(data)

def get_property_detail(request, pk):
	context = {
		'pk' : pk
	}
	return render(request, 'rentals/property_detail.html', context)


class ListCreatePropertyUnit(ListCreateAPIView):
	queryset = rental_models.PropertyUnit.objects.order_by('name')
	serializer_class = rental_serializers.PropertyUnitSerializer

class PropertyUnitDetail(RetrieveUpdateDestroyAPIView):
	queryset = rental_models.PropertyUnit.objects.order_by('name')
	serializer_class = rental_serializers.PropertyUnitSerializer
	lookup_field = 'pk'

def get_tenants(request):
	return render(request, 'rentals/tenants.html')

class ListCreateTenants(ListCreateAPIView):
	queryset = rental_models.Tenant.objects.order_by('name')
	serializer_class = rental_serializers.TenantsSerializer

class TenantDetail(RetrieveUpdateDestroyAPIView):
	queryset = rental_models.Tenant.objects.order_by('name')
	serializer_class = rental_serializers.TenantsSerializer
	lookup_field = 'pk'
