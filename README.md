## DDCBack
1) Установка зависимостей:
  Проект создавался с использованием python, фреймворк django. Необходимо выполнить команду pip install django для использования.Так же, для просмотра базы данных необходимо(или желательно) установить SQLView.
2) Настройка базы данных
  В проекте уже существует база данных, при создании БД с нуля необходимо удалить уже существующую базу и использовать команды python manage.py makemigrations, а затем python manage.py migrate.
   При существовании базы(соответствующей или нет моделям) необходимо удалить существующую БД и в списке DDC/settings -> словарь DATABASES изменить название стандартной БД. Выполнить команды миграции(python manage.py makemigrations, python manage.py migrate).
   В проекте уже существует суперпользователь и предусмотрено создание строк в БД через страницу админа. Логин - root, пароль - root. При удалении БД необходимо заново создать суперпользователя: python manage.py createsuperuser и следовать инструкциям по созданию пользователя. Переход на страницу: localhost/admin/
3) Запуск веб-сервиса:
   cd DDC - переход в папку проекта
  python manage.py runserver - запуск проекта и переход по ссылке откроет веб-сервис в локальном режиме
