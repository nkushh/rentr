from django.urls import path
from . import views

app_name = 'system_admin'

urlpatterns = [
	# Property categories
	path('property-categories/', views.property_categories, name='property_categories'),
	path('property-category/', views.ListCreatePropertyCategory.as_view(), name='property_category'),
	path('property-category-detail/<int:pk>/', views.PropertyCategoryDetail.as_view(), name='property_category_detail'),
	# Property types
	path('property-types/', views.property_types, name='property_types'),
	path('property-type/', views.ListCreatePropertyType.as_view(), name='property_type'),
	path('property-type-detail/<int:pk>/', views.PropertyTypeDetail.as_view(), name='property_type_detail'),
]