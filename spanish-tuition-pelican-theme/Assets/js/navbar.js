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
    $('a[href^="#"').bind('click', function(event) {
        //Make navbar auto-collapse on mobile
        if ($('.navbar-toggle').is(':visible') && $('.navbar-main-collapse').is(':visible'))
            $('.navbar-toggle').click();

        var $anchor = $(this),
            targetEl = $($anchor.attr('href')),
            offset = (targetEl.prop('tagName') === 'SECTION') ? 0 : 80;

        $('html, body').stop().animate({
            scrollTop: targetEl.offset().top - offset
        }, 1500, 'jswing');
        event.preventDefault();
    });

    //Will toggle the class for the navbar-header
    //so that when in mobile, if the drop down menu
    //is activated, the navbar's background color will
    //change
    $("#dropdown-menu").on('click', function() {
        $("#navbar-header").toggleClass("dropdown-menu");
    });
})
