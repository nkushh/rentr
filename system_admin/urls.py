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
	# Deposit categories
	path('get-deposit-categories/', views.get_deposit_categories, name='get_deposit_categories'),
	path('deposit-categories/', views.ListCreateDepositCharge.as_view(), name='deposit_categories'),
	path('deposit-category-detail/<int:pk>/', views.DepositCategoryDetail.as_view(), name='deposit_category_detail'),
	# Recharge charges
	path('get-recurrent-charges/', views.get_recurrent_charges, name='get_recurrent_charges'),
	path('recurrent-charges/', views.ListCreateRecurrentCharge.as_view(), name='recurrent_charges'),
	path('recurrent-charge-detail/<int:pk>/', views.RecurrentChargeDetail.as_view(), name='recurrent_charge_detail'),
]