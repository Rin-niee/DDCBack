from django import forms
from .models import *
from datetime import datetime
from django.utils import timezone


class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'count_sum', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not self.instance.date:
            self.fields['date'].initial = timezone.now()

        # Если объект уже существует (редактирование), загружаем категории и подкатегории
        if self.instance.pk:  
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type).order_by('name')
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category).order_by('name')
        else:
            self.fields['category'].queryset = Category.objects.none()
            self.fields['subcategory'].queryset = Subcategory.objects.none()

        # Если форма отправляется (POST-запрос), подгружаем данные динамически
        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id).order_by('name')
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {'type': forms.Select(attrs={'class': 'type-select'})}  # Выпадающий список типов

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {'category': forms.Select(attrs={'class': 'category-select'})}  # Выпадающий список категорий