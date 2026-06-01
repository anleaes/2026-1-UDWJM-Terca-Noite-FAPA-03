from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'audit_reports'

router = routers.SimpleRouter()
router.register('', views.AuditReportViewSet, basename='audit_reports')

urlpatterns = [
    path('add/', views.add_audit_report, name='add_audit_report'),
    path('list/', views.list_audit_report, name='list_audit_report'),
    path('edit/<int:id_audit_report>/', views.edit_audit_report, name='edit_audit_report'),
    path('delete/<int:id_audit_report>/', views.delete_audit_report, name='delete_audit_report'),
    path('', include(router.urls)),
]
