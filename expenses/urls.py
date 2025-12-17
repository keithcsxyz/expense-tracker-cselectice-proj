from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add'),
    path('edit/<int:pk>/', views.edit_expense, name='edit'),
    path('delete/<int:pk>/', views.delete_expense, name='delete'),
    path('export_csv/', views.export_csv, name='export_csv'),
]
