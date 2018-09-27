window.onload = function () {
    $(".positions").on('click', 'input[type=number]', function () {
        $.ajax({
            url: "/order/edit/" + event.target.name + "/" + event.target.value + "/",
            success: function (data) {
                $('.positions').html($(data.result).find('table').html());
            },
        });
        event.preventDefault();
    });
}