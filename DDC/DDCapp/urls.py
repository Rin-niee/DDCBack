from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"), #URL исходной страницы
    path('entry/', views.entry, name='entry'), #URL страницы создания
    path('entry/<int:id>/', views.entry, name='edit_cashflow'), #URL страницы редактирования(по id объекта)
    path('control/', views.control, name = "control"), #URL страницы создания статусов/типов/категорий/подкатегорий
    path('delete/<str:model_name>/<int:pk>/', views.delete_entry, name='delete_entry'), #удаление статусов/типов/категорий/подкатегорий(модальное окно)
    path('delete/<int:cashflow_id>/', views.cashflow_delete, name='cashflow_delete'),#удаление статей(модальное окно)
    path('ajax/load-categories/', views.load_categories, name='load_categories'), #загрузка категорий для типов
    path('ajax/load-subcategories/', views.load_subcategories, name='load_subcategories'),#загрузка подкатегорий для категорий
]
