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

list_btn.addEventListener('click', showList);
map_btn.addEventListener('click', hideList);

function showList() {
    list_container.classList.add('showing');
    list_btn.classList.add('none');
    map_btn.classList.remove('none');
}

function hideList() {
    list_container.classList.remove('showing');
    list_btn.classList.remove('none');
    map_btn.classList.add('none');
}


