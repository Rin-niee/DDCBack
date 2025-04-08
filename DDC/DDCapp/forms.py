from django import forms
from .models import *
from django.utils import timezone

#модель необходимой таблицы
class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'status', 'type', 'category', 'subcategory', 'count_sum', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['status'].empty_label = 'Выберите статус'
        self.fields['type'].empty_label = 'Выберите тип'
        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['subcategory'].empty_label = 'Выберите подкатегорию'
        self.fields['count_sum'].widget.attrs['placeholder']= 'Введите сумму'
        self.fields['comment'].widget.attrs['placeholder']= 'Введите комментарий'
        
        if not self.instance.date:
            self.fields['date'].initial = timezone.now()

        # Редактирование моделей. Загрузка подкатегорий и категорий из БД
        if self.instance.pk:  
            self.fields['category'].queryset = Category.objects.filter(type=self.instance.type).order_by('name')
            self.fields['subcategory'].queryset = Subcategory.objects.filter(category=self.instance.category).order_by('name')
        else:
            self.fields['category'].queryset = Category.objects.none()
            self.fields['subcategory'].queryset = Subcategory.objects.none()
        #обновление списков в соответствии с выбранными зависимостями(тип - категория, категория - подкатегория)
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

#форма модели статусов(создание)
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder']= 'Название статуса'

#форма модели типов(создание)
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder']= 'Название типа'

#форма модели категорий(создание)
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {'type': forms.Select(attrs={'class': 'type-select'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['type'].empty_label = 'Выберите тип'
        self.fields['name'].widget.attrs['placeholder']= 'Название категории'


#форма модели подкатегорий(создание)
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        widgets = {'category': forms.Select(attrs={'class': 'category-select'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['name'].widget.attrs['placeholder']= 'Название подкатегории'