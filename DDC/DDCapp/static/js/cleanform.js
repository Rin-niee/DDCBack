$(document).ready(function() {
    $('.empty_btn').click(function(e) {
        e.preventDefault();
        $('#brand').val('');
        $('#model').html('<option value="">Модель авто</option>');
        $('#category').val('');
        $('#subcategory').html('<option value="">Подкатегория</option>');
        $('#type').val('');
        localStorage.removeItem('selectedBrand');
        localStorage.removeItem('selectedModel');
        localStorage.removeItem('selectedCategory');
        localStorage.removeItem('selectedSubcategory');
        localStorage.removeItem('selectedType');
        const targetPage = $(this).data('target-url');
        if (window.location.href !== targetPage) {
            window.location.href = targetPage;
        }
    });
});
