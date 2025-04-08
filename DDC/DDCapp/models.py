from django.db import models

# Create your models here.
#датазаписи(01.01.2025), 
# статус(бизнес, личное, налог, !список может расширяться!), 
# категория и подкатегория, типКатегория “Инфраструктура” (подкатегории: "VPS", "Proxy")Категория “Маркетинг” (подкатегории: "Farpost", "Avito") Данный список должен иметь возможность расширяться, 
# сумма(количество средств в рублях, например, 1 000 р.:), 
# комментарий(в свободной форме, не обязателен к заполнению)

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Типы денежных операций
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Категории с привязкой к типу
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(Type, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Подкатегории с привязкой к категории
class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Основная модель CashFlow для учета движения денежных средств
class CashFlow(models.Model):
    date = models.DateTimeField()  # Дата записи
    status = models.ForeignKey(Status, on_delete=models.CASCADE)  # Статус
    type = models.ForeignKey(Type, on_delete=models.CASCADE)  # Тип (Пополнение, Списание)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)  # Подкатегория
    count_sum = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма
    comment = models.TextField(blank=True, null=True)  # Комментарий

    def __str__(self):
        return f"CashFlow {self.id} - {self.count_sum} руб"