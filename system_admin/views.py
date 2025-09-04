from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render
# Models
from . import models as admin_models
# Serializers
from . import serializers as admin_serializers

# Create your views here.
def property_categories(request):
	return render(request, 'system_admin/property_categories.html')

class ListCreatePropertyCategory(ListCreateAPIView):
	queryset = admin_models.PropertyCategory.objects.order_by('name')
	serializer_class = admin_serializers.PropertyCategorySerializer

class PropertyCategoryDetail(RetrieveUpdateDestroyAPIView):
	queryset = admin_models.PropertyCategory.objects.order_by('name')
	serializer_class = admin_serializers.PropertyCategorySerializer
	lookup_field = 'pk'

def property_types(request):
	property_categories = admin_models.PropertyCategory.objects.order_by('name')
	context = {
		'property_categories' : property_categories
	}
	return render(request, 'system_admin/property_types.html', context)

class ListCreatePropertyType(ListCreateAPIView):
    queryset = admin_models.PropertyType.objects.select_related('property_category').order_by('name')
    serializer_class = admin_serializers.PropertyTypeSerializer
    
class PropertyTypeDetail(RetrieveUpdateDestroyAPIView):
	queryset = admin_models.PropertyType.objects.select_related('property_category').order_by('name')
	serializer_class = admin_serializers.PropertyTypeSerializer
	lookup_field = 'pk'