/**
 * Created by Stepan on 07.01.15.
 */
$(document).ready(function(){
    $('.bxslider').bxSlider({
        auto: true
    });
    var imagesPerPage = 6;

    $('.quest-gallery').each(function(i, el){
        var shift = 150;
        var itter = 0;
        $('#' + $(this).attr('id')).magnificPopup({
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
        var amount = $(el).find('li').length;
        setDisablePrevNext(itter, amount, $(el));
        $(el).find('.next').click(function(){
            if ($(this).hasClass('disable')) {
                return;
            }
            var left = parseInt($(el).find('ul').css('left')) * (-1);
            move($(el).find('ul'), left, left + shift, true);
            itter++;
            setDisablePrevNext(itter, amount, $(el));
        });
        $(el).find('.prev').click(function(){
            if ($(this).hasClass('disable')) {
                return;
            }
            var left = parseInt($(el).find('ul').css('left')) * (-1);
            move($(el).find('ul'), left, left - shift, false);
            itter--;
            setDisablePrevNext(itter, amount, $(el));
        });
    });

    function setDisablePrevNext(itter, amount, $ul) {
        if (amount - itter - imagesPerPage <= 0) {
            $ul.find('.next').addClass('disable');
        } else {
            $ul.find('.next').removeClass('disable');
        }
        if (itter) {
            $ul.find('.prev').removeClass('disable');
        } else {
            $ul.find('.prev').addClass('disable');
        }
    }

    function move($el, start, end, increase) {
        var timer = setInterval(function(){
            if (increase) {
                if (start < end) {
                    start += 5;
                    $el.css('left', '-' + start + 'px');
                } else {
                    clearInterval(timer);
                }
            } else {
                if (start > end) {
                    start -= 5;
                    $el.css('left', '-' + start + 'px');
                } else {
                    clearInterval(timer);
                }
            }
        }, 10);
    }

});