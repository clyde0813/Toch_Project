$(document).ready(function(){
    $('.hover').hover(function(){
        $(this).children('div').stop().slideDown()
    },function(){
        $(this).children('div').stop().slideUp()
    });

    $('.heartIcon').click(function(){
        $(this).toggleClass('active');
    })
})