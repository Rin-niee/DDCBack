from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
   path('entry/', views.entry, name='entry'),  # Создание/редактирование записи
    path('entry/<int:id>/', views.entry, name='edit_cashflow'),  # Редактирование записи
    path('control/', views.control, name = "control"),\
    path('delete/<str:model_name>/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('delete/<int:cashflow_id>/', views.cashflow_delete, name='cashflow_delete'),
    path('ajax/load-categories/', views.load_categories, name='load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='load_subcategories'),
]
