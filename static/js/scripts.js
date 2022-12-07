$(function(){
    $('.basket_list input').change(function(){
        let q = this;
        if (q.value < 0) q.value = 0;
        $.ajax({
            url: '/basket/edit/' + q.name + '/' + q.value + '/',
            success: function(data) {
                if (data.result > 0) {
                    q.value = data.result;
                } else {
                    $(q).parents('tr').remove();
                    if (!$('.basket_list td').length) {
                        $('.basket_list').after('<p>В корзине пусто.</p>').remove();
                    }
                }
            }
        });
    });
});