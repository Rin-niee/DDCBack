$(document).ready(function() {
        function loadCategories(type_id) {
            if (type_id) {
                $.ajax({
                    url: '/ajax/load-categories/',
                    data: {'type_id': type_id},
                    success: function(data) {
                        $('#category').html('<option value="">Выберите категорию</option>');
                        $.each(data, function(index, category) {
                            $('#category').append('<option value="' + category.id + '">' + category.name + '</option>');
                        });
                        $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
                    }
                });
            } else {
                $('#category').html('<option value="">Выберите категорию</option>');
                $('#subcategory').html('<option value="">Выберите подкатегорию</option>');
            }
        }
        function loadSubcategories(category_id) {
            if (category_id) {
                $.ajax({
                    url: '/ajax/load-subcategories/',
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

        $('#type').change(function() {
            var type_id = $(this).val();
            loadCategories(type_id);
        });

        $('#category').change(function() {
            var category_id = $(this).val();
            loadSubcategories(category_id);
        });

        var savedType = $('#type').val();
        if (savedType) {
            loadCategories(savedType);
        }
        
        var savedCategory = $('#category').val();
        if (savedCategory) {
            loadSubcategories(savedCategory);
        }
    });
