$(document).ready(function(){
    /* $('[data-click]').click(function(){
        var selector = $('.' + $(this).attr('data-click'));
        selector.addClass('active');
        selector.find('.close').click(function(){
            selector.removeClass('active');
        });
    }); */

    $('[data-click="gnbSearchBox"]').click(function(){
        var selector = $('.gnbSearchBox');
        selector.addClass('active');
        selector.find('.close').click(function(){
            selector.removeClass('active');
        });
    });

    $('[data-click="next"]').click(function(){
        $(this).toggleClass('active');
        $(this).next().slideToggle();
    })

    $('[data-popup]').click(function(e){
        e.preventDefault();
        var selector = $('.' + $(this).attr('data-popup'));
        selector.addClass('active');

        selector.click(function(){
            selector.removeClass('active');
        });
        selector.children('div').click(function(e){
            e.stopPropagation();
        })
        selector.find('button').click(function(){
            selector.removeClass('active');
        });
    });
})