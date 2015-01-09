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

    function disableTimeOrders() {
        $('.time input[name=time]').prop('checked', false).prop('disabled', false);
        var $datepicker = $("#datepicker");
        var targetDate = $datepicker.datepicker({ dateFormat: 'dd-mm-yy' }).val();
        var DD = $.datepicker.formatDate('DD', new Date(targetDate));
        var monthNum = $datepicker.datepicker('getDate').getMonth();
        var dayNum = $datepicker.datepicker('getDate').getDate();
        var text = dayNum + " " + genitive[monthNum] + ", " + DD;
        $('.fields .date').text(text);
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

    function addAvailable(refresh) {
        if (refresh) {
            $("#datepicker").datepicker("refresh");
        }
        var selectedQuest = $('[name=quest] option:selected');
        var times = null;
        for (var i = 0; i < schedule.length; i++) {
            if (schedule[i].questId == selectedQuest.val()) {
                times = schedule[i].times.length;
                break;
            }
        }
        var tdDate = null;
        $('.available-time').remove();
        $("#datepicker").find('td:not(.ui-state-disabled)').each(function(i, el){
            var currentTimes = times;
            var available = 0;
            var tdDate =
                $.datepicker.formatDate(
                    "yy-mm-dd",
                    new Date(
                        $(el).data('year'),
                        $(el).data('month'),
                        $(el).text()
                    )
                );
            for (var i = 0; i < orders.length; i++) {
                if (
                    orders[i].fields.date == tdDate &&
                        orders[i].fields.quest == selectedQuest.val()
                ) {
                    currentTimes--;
                }
            }
            var $time = $('.' + tdDate + '.available-time');
            if (!$time.length) {
                $('body').append('<div class="' + tdDate + ' available-time">Осталось игр: <span class="game-amount"></span></div>');
                $time = $('.' + tdDate + '.available-time');
            }
            var top = $(this).find('.ui-state-default').offset()['top'] + 18;
            var left = $(this).find('.ui-state-default').offset()['left'];
            $time.css('top', top + "px");
            $time.css('left', left + "px");
            $time.find('.game-amount').text(currentTimes);
            $time.click(function(){
                $(el).find('a').click();
            });
        });
    }

    $.datepicker.setDefaults($.extend($.datepicker.regional["ru"]));
    $("#datepicker")
        .datepicker({
            dateFormat: "yy-mm-dd",
            minDate: 0,
            maxDate: "+6D",
            onSelect: function (date, inst) {
                disableTimeOrders();
                setTimeout(
                    function() {addAvailable(false)},
                    50
                );
            },
            onChangeMonthYear: function() {
                disableTimeOrders();
                setTimeout(
                    function() {addAvailable(false)},
                    50
                );
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
        setTimes();
        disableTimeOrders();
        addAvailable(true);
    });

    function setTimes() {
        var selectedQuest = $('[name=quest] option:selected');
        for (var i = 0; i < schedule.length; i++) {
            if (schedule[i].questId != selectedQuest.val()) {
                continue;
            }
            $('.fields .time').html("");
            for (var j = 0; j < schedule[i].times.length; j++) {
                $('.fields .time').append(
                    "<div><label><input type='radio' name='time' value='" + schedule[i].times[j].id + "'/>" + schedule[i].times[j].time + "</label></div>"
                );
            }
        }
    }

    function init() {
        setTimes();
        disableTimeOrders();
        addAvailable(false);
    }
    init();
});