from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('list/', views.list_employees, name='list_employees'),
]
