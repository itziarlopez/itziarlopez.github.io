$(function() {
    
    //jQuery to collapse the navbar on scroll
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 0) {
            $(".navbar-fixed-top").addClass("top-navbar-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-navbar-collapse");
        }
    });

    //jQuery for page scrolling feature - requires jQuery Easing plugin
    $('a[href=#page-top], a[href=#corporate], a[href=#about], a[href=#adults], a[href=#teens], a[href=#children], a[href=#contact]').bind('click', function(event) {
        //Make navbar auto-collapse on mobile
        if ($('.navbar-toggle').is(':visible') && $('.navbar-main-collapse').is(':visible'))
            $('.navbar-toggle').click();

        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'jswing');
        event.preventDefault();
    });
})