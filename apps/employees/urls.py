from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('list/', views.list_employee, name='list_employee'),
    path('edit/<int:id_employee>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:id_employee>/', views.delete_employee, name='delete_employee'),
]
