$(document).ready(function() {
    $('.empty_btn').click(function(e) {
        e.preventDefault(); // Предотвращает стандартное поведение кнопки

        // Очищаем поля бренда и модели
        $('#brand').val('');
        $('#model').html('<option value="">Модель авто</option>');  // Очищаем список моделей

        // Очищаем поля категории, подкатегории и типа
        $('#category').val('');
        $('#subcategory').html('<option value="">Подкатегория</option>');  // Очищаем список подкатегорий
        $('#type').val('');

        // Удаляем все сохраненные данные из localStorage
        localStorage.removeItem('selectedBrand');
        localStorage.removeItem('selectedModel');
        localStorage.removeItem('selectedCategory');
        localStorage.removeItem('selectedSubcategory');
        localStorage.removeItem('selectedType');

        // Получаем целевой URL из атрибута data-target-url
        const targetPage = $(this).data('target-url');

        // Проверяем текущий URL
        if (window.location.href !== targetPage) {
            // Если текущая страница не целевая, переходим на целевую страницу
            window.location.href = targetPage;
        } else {
            // Если уже на целевой странице, ничего не делаем
            // console.log("Вы уже на целевой странице.");
        }
    });
});
