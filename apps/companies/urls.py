from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('add/', views.add_company, name='add_company'),
    path('list/', views.list_companies, name='list_companies'),
    path('edit/<int:id_company>/', views.edit_company, name='edit_company'),
    path('delete/<int:id_company>/', views.delete_company, name='delete_company'),
]
