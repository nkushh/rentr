from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
	# Properties
	path('properties/', views.properties, name='properties'),
	path('property-list/', views.ListCreateProperty.as_view(), name='property_list'),
	path('get-property-detail/<int:pk>/', views.get_property_detail, name='get_property_detail'),
	path('property-detail/<int:pk>/', views.PropertyDetail.as_view(), name='property_detail'),
	path('property-config/<int:pk>/', views.PropertyConfigView.as_view(), name='property_config'),
	# Property units
	path('property-units/', views.ListCreatePropertyUnit.as_view(), name='property_units'),
	path('property-unit-detail/<int:pk>/', views.PropertyUnitDetail.as_view(), name='property_unit_detail'),
	# Tenants
	path('get-tenants/', views.get_tenants, name='get_tenants'),
	path('tenants/', views.ListCreateTenants.as_view(), name='tenants'),
	path('tenant-detail/<int:pk>/', views.TenantDetail.as_view(), name='tenant_detail'),
]