const cart_reload = () => {
    $.get("/order/cart/", function (data) {
        $('.cart').parent('li').html(data.result)
    });
}
window.onload = function () {
    $(".positions").on('click', 'input[type=number]', function () {
        $.get("/order/edit/" + event.target.name + "/" + event.target.value + "/", function (data) {
            $('.positions').html(data.result)
            cart_reload();
        });
        event.preventDefault();
    });
    $(".positions").on('click', '[data-remove-url]', function () {
        $.get($(this).data('removeUrl'), function (data) {
            $('.positions').html(data.result)
            cart_reload();
        });
        event.preventDefault();
    });
}