from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'inspections'

router = routers.SimpleRouter()
router.register('', views.InspectionViewSet, basename='inspections')

urlpatterns = [
    path('add/', views.add_inspection, name='add_inspection'),
    path('list/', views.list_inspection, name='list_inspection'),
    path('edit/<int:id_inspection>/', views.edit_inspection, name='edit_inspection'),
    path('delete/<int:id_inspection>/', views.delete_inspection, name='delete_inspection'),
    path('', include(router.urls)),
]
