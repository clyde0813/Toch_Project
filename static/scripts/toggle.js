$(document).ready(function () {
    $('[data-popup]').click(function (e) {
        e.preventDefault();
        $('[class*="box"]').removeClass('active');
        var popupArea = $(this).siblings('.' + $(this).attr('data-popup'));
        if (popupArea.length == 0) {
            popupArea = $('.' + $(this).attr('data-popup'));
        }
        popupArea.addClass('active');
        popupArea.click(function (e) {
            e.stopPropagation();
        })
        popupArea.find('.closeBtn').click(function () {
            popupArea.removeClass('active')
        })
        popupArea.children('div').click(function (e) {
            e.stopPropagation();
        })
    })
})