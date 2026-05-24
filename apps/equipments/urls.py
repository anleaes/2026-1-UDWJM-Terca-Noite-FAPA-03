from django.urls import path
from . import views

app_name = 'equipments'

urlpatterns = [
    path('<int:company_id>/list/', views.list_equipments, name='list_equipments'),
    path('<int:company_id>/add/', views.add_equipment, name='add_equipment'),
    path('<int:company_id>/edit/<int:equipment_id>/', views.edit_equipment, name='edit_equipment'),
    path('<int:company_id>/delete/<int:equipment_id>/', views.delete_equipment, name='delete_equipment'),
]
