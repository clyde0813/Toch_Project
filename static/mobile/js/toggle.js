$(document).ready(function () {
    $('[data-popup2]').click(function (e) {
        e.preventDefault();
        $('[class*="box"]').removeClass('active');
        var popupArea = $(this).siblings('.' + $(this).attr('data-popup2'));
        if (popupArea.length == 0) {
            popupArea = $('.' + $(this).attr('data-popup2'));
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