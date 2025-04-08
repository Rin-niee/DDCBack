$(document).ready(function() {
        // Функция для загрузки категорий на основе типа
        function loadCategories(type_id) {
            if (type_id) {
                $.ajax({
                    url: '/ajax/load-categories/',  // Путь для асинхронной загрузки категорий
                    data: {'type_id': type_id},
                    success: function(data) {
                        $('#category').html('<option value="">Выберите категорию</option>');
                        $.each(data, function(index, category) {
                            $('#category').append('<option value="' + category.id + '">' + category.name + '</option>');
                        });

                        // После загрузки категорий очищаем подкатегории
                        $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
                    }
                });
            } else {
                $('#category').html('<option value="">Выберите категорию</option>');
                $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
            }
        }

        // Функция для загрузки подкатегорий на основе категории
        function loadSubcategories(category_id) {
            if (category_id) {
                $.ajax({
                    url: '/ajax/load-subcategories/',  // Путь для асинхронной загрузки подкатегорий
                    data: {'category_id': category_id},
                    success: function(data) {
                        $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
                        $.each(data, function(index, subcategory) {
                            $('#subcategory').append('<option value="' + subcategory.id + '">' + subcategory.name + '</option>');
                        });
                    }
                });
            } else {
                $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
            }
        }

        // При изменении типа
        $('#type').change(function() {
            var type_id = $(this).val();
            loadCategories(type_id);  // Загружаем категории на основе выбранного типа
        });

        // При изменении категории
        $('#category').change(function() {
            var category_id = $(this).val();
            loadSubcategories(category_id);  // Загружаем подкатегории на основе выбранной категории
        });

        // Если тип уже выбран на странице, загружаем соответствующие категории
        var savedType = $('#type').val();
        if (savedType) {
            loadCategories(savedType);
        }

        // Если категория уже выбрана, загружаем соответствующие подкатегории
        var savedCategory = $('#category').val();
        if (savedCategory) {
            loadSubcategories(savedCategory);
        }
    });
