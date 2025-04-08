$(document).ready(function() {
    var selectedTypeId = $('#id_type').val();
    var selectedCategoryId = $('#id_category').val();
    var selectedSubcategoryId = $('#id_subcategory').val();

    if (selectedTypeId) {
        loadCategories(selectedTypeId, selectedCategoryId, false);
    }
    if (selectedCategoryId) {
        loadSubcategories(selectedCategoryId, selectedSubcategoryId, false);
    }

    $('#id_type').change(function() {
        var type_id = $(this).val();
        if (type_id) {
            loadCategories(type_id, null, true);
        } else {
            $('#id_category').html('<option value="">Выберите категорию</option>');
            $('#id_subcategory').html('<option value="">Выберите подкатегорию</option>');
        }
    });

    $('#id_category').change(function() {
        var category_id = $(this).val();
        if (category_id) {
            loadSubcategories(category_id, null, true);
        } else {
            $('#id_subcategory').html('<option value="">Выберите подкатегорию</option>');
        }
    });

    function loadCategories(type_id, selectedCategoryId, clearSubcategory) {
        $.ajax({
            url: '/ajax/load-categories/',
            data: { 'type_id': type_id },
            success: function(data) {
                $('#id_category').html('<option value="">Выберите категорию</option>');
                $.each(data, function(index, category) {
                    $('#id_category').append('<option value="' + category.id + '">' + category.name + '</option>');
                });
                if (selectedCategoryId) {
                    $('#id_category').val(selectedCategoryId);
                }
                if (clearSubcategory) {
                    $('#id_subcategory').html('<option value="">Выберите подкатегорию</option>');
                }
            }
        });
    }

    function loadSubcategories(category_id, selectedSubcategoryId, clearSelection) {
        $.ajax({
            url: '/ajax/load-subcategories/',
            data: { 'category_id': category_id },
            success: function(data) {
                $('#id_subcategory').html('<option value="">Выберите подкатегорию</option>');
                $.each(data, function(index, subcategory) {
                    $('#id_subcategory').append('<option value="' + subcategory.id + '">' + subcategory.name + '</option>');
                });
                if (selectedSubcategoryId) {
                    $('#id_subcategory').val(selectedSubcategoryId);
                }
            }
        });
    }
});
