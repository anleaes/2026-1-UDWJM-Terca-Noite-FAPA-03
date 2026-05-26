from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('add/', views.add_location, name='add_location'),
    path('list/', views.list_location, name='list_location'),
    path('edit/<int:id_location>/', views.edit_location, name='edit_location'),
    path('delete/<int:id_location>/', views.delete_location, name='delete_location'),
]
