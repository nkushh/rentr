from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
	# Property categories
	path('property-categories/', views.property_categories, name='property_categories'),
	path('property-category/', views.ListCreatePropertyCategory.as_view(), name='property_category'),
	path('property-category-detail/<int:pk>/', views.PropertyCategoryDetail.as_view(), name='property_category_detail'),
	# Property types
	path('property-types/', views.property_types, name='property_types'),
	path('property-type/', views.ListCreatePropertyType.as_view(), name='property_type'),
	path('property-type-detail/<int:pk>/', views.PropertyTypeDetail.as_view(), name='property_type_detail'),
	# Properties
	path('properties/', views.properties, name='properties'),
	path('property-list/', views.ListCreateProperty.as_view(), name='property_list'),
	path('get-property-detail/<int:pk>/', views.get_property_detail, name='get_property_detail'),
	path('property-detail/<int:pk>/', views.PropertyDetail.as_view(), name='property_detail'),
	# Property units
	path('property-units/', views.ListCreatePropertyUnit.as_view(), name='property_units'),
	path('property-unit-detail/<int:pk>/', views.PropertyUnitDetail.as_view(), name='property_unit_detail'),
]