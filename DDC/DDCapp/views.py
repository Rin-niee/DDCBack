from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from datetime import datetime
from django.db.models import Q
from django.contrib import messages

def cashflow_delete(request, cashflow_id):
    cashflow = get_object_or_404(CashFlow, id=cashflow_id)
    cashflow.delete()
    messages.success(request, "Запись успешно удалена.")
    return redirect('index')  # или другой URL, куда редиректить

#главная страница
def index(request):
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    # Фильтрация по параметрам
    cashflows = CashFlow.objects.all()

    # Фильтрация по датам (начальная и конечная дата)
    unique_dates = CashFlow.objects.values_list('date', flat=True).distinct()

    # Фильтрация по статусу
    status_id = request.GET.get('status')
    if status_id:
        cashflows = cashflows.filter(status_id=status_id)

    # Фильтрация по типу
    type_id = request.GET.get('type')
    if type_id:
        cashflows = cashflows.filter(type_id=type_id)

    # Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        cashflows = cashflows.filter(category_id=category_id)

    # Фильтрация по подкатегории
    subcategory_id = request.GET.get('subcategory')
    if subcategory_id:
        cashflows = cashflows.filter(subcategory_id=subcategory_id)

    # Получаем категории для выбранного типа
    if type_id:
        categories = categories.filter(type_id=type_id)

    # Получаем подкатегории для выбранной категории
    if category_id:
        subcategories = subcategories.filter(category_id=category_id)
    context ={
        'unique_dates': unique_dates,
        'statuses': statuses,
        'cashflows': cashflows,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'index.html', context)

#страница создания/редактирования
def entry(request, id=None):
    cashlil = None
    if id:
        # Если передан ID, редактируем существующую запись
        cashlil = get_object_or_404(CashFlow, id=id)
        if request.method == 'POST':
            form = CashFlowForm(request.POST, instance=cashlil)
            if form.is_valid():
                form.save()
                return redirect('index')  # Перенаправление после сохранения
        else:
            form = CashFlowForm(instance=cashlil)
            if cashlil.date:
                form.fields['date'].initial = cashlil.date.strftime('%Y-%m-%d')
    else:
        # Создание новой записи
        if request.method == 'POST':
            form = CashFlowForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')  # Перенаправление после создания
        else:
            form = CashFlowForm()

    context = {
        'form': form,
        'cashlil': cashlil
    }
    return render(request, 'entry.html', context)

#редактура колонок
def control(request):
    # Формы
    status_form = StatusForm(request.POST or None)
    type_form = TypeForm(request.POST or None)
    category_form = CategoryForm(request.POST or None)
    subcategory_form = SubcategoryForm(request.POST or None)

    # Если POST -> сохраняем
    if request.method == 'POST':
        # Проверяем, какая форма была отправлена
        if 'status_form' in request.POST and status_form.is_valid():
            status_form.save()
        elif 'type_form' in request.POST and type_form.is_valid():
            type_form.save()
        elif 'category_form' in request.POST and category_form.is_valid():
            category_form.save()
        elif 'subcategory_form' in request.POST and subcategory_form.is_valid():
            subcategory_form.save()

        # Редирект после сохранения формы
        return redirect('control')

    # Отправляем данные в шаблон
    context = {
        'statuses': Status.objects.all(),
        'types': Type.objects.prefetch_related('categories'),
        'categories': Category.objects.prefetch_related('subcategories'),
        'subcategories': Subcategory.objects.all(),
        'status_form': status_form,
        'type_form': type_form,
        'category_form': category_form,
        'subcategory_form': subcategory_form,
    }
    return render(request, 'control.html', context)


def delete_entry(request, model_name, pk):
    models = {'status': Status, 'type': Type, 'category': Category, 'subcategory': Subcategory}
    model = models.get(model_name)
    if model:
        obj = get_object_or_404(model, pk=pk)
        obj.delete()
    return redirect('control')



def get_subcategories(request):
    category_id = request.GET.get('category_id')  # Получаем ID категории
    if category_id:
        subcategories = Subcategory.objects.filter(category_id=category_id)
    else:
        subcategories = []
    # Формируем ответ
    data = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]
    return JsonResponse({'subcategories': data})



def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id)
    category_list = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(category_list, safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id)
    subcategory_list = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]
    return JsonResponse(subcategory_list, safe=False)