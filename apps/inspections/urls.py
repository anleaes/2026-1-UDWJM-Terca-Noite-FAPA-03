from django.urls import path
from . import views

app_name = 'inspections'

urlpatterns = [
    path('add/', views.add_inspection, name='add_inspection'),
    path('list/', views.list_inspection, name='list_inspection'),
    path('edit/<int:id_inspection>/', views.edit_inspection, name='edit_inspection'),
    path('delete/<int:id_inspection>/', views.delete_inspection, name='delete_inspection'),
]
