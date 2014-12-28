/**
 * Created by Stepan on 22.12.14.
 */
$(document).ready(function(){
    var genitive = [
        "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
        "августа", "сентября", "октября", "ноября", "декабря"
    ];

    var months = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
        "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ];

    $('.bxslider').bxSlider({
        auto: true
    });

    $('.quest-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		}
	});

    function disableTimeOrders() {
        $('.time input[name=time]').prop('checked', false).prop('disabled', false);
        var targetDate = $("#datepicker").datepicker({ dateFormat: 'dd-mm-yy' }).val();
        $('input[name=date]').val(targetDate);
        for (var i = 0; i < orders.length; i++) {
            if (
                orders[i].fields.date == targetDate &&
                    orders[i].fields.quest == $('select.quest').val()
                ) {
                $('.time input[name=time]').each(function(){
                    if ($(this).val() == orders[i].fields.time) {
                        $(this).prop('disabled', 'disabled');
                    }
                });
            }
        }
    }

    $.datepicker.setDefaults($.extend($.datepicker.regional["ru"]));
    $("#datepicker").datepicker({
        dateFormat: "yy-mm-dd",
        minDate: 0,
        maxDate: "+1M +10D",
        onSelect: function (date, inst) {
            disableTimeOrders();
        }
    });

    $('.submit').click(function() {
        event.preventDefault();
        event.stopPropagation();
        var isEmpty = false;
        $('input[type=text]').each(function(){
            if ($.trim($(this).val()) == "") {
                isEmpty = true;
            }
        });
        if ($('[type=radio]:checked').length == 0) {
            isEmpty = true;
        }
        if (isEmpty) {
            alert("Пожалуйста, заполните все поля");
            return;
        }
        $('#order').ajaxSubmit({
            success: function() {
                alert('Ваша заявка принята');
            },
            error: function() {
                alert('Произошла ошибка');
            }
        });
    });

    $('select.quest').change(function(){
        disableTimeOrders();
    });

    function init() {
        disableTimeOrders();
    }
    init();
});