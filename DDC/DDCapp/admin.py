from django.contrib import admin
from .models import Status, Type, Category, Subcategory, CashFlow

#можно добавлять данные через панель администратора
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(CashFlow)