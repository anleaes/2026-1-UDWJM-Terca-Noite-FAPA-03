from django.urls import path
from . import views

app_name = 'constructionequipments'

urlpatterns = [
    path('add/', views.add_constructionequipment, name='add_constructionequipment'),
    path('list/', views.list_constructionequipment, name='list_constructionequipment'),
    path('edit/<int:id_constructionequipment>/', views.edit_constructionequipment, name='edit_constructionequipment'),
    path('delete/<int:id_constructionequipment>/', views.delete_constructionequipment, name='delete_constructionequipment'),
]
