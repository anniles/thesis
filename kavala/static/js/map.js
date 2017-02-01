(function() {
    "use strict";


    $('.map-btn').on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();

        if( !($('.my_collapse').hasClass('in')) ) {
            $('.my_collapse').addClass('in');
            $('html,body').animate({
                scrollTop: $('.map-btn').offset().top-50},
                500);
            setTimeout(function() {
                $('#map').css('z-index', '1')
            }, 500);
            initMap();
        }else {
            $('#map').css('z-index', '-1')

            var offset = $('.map-btn').offset();

            $('.my_collapse').removeClass('in');
            $('html,body').animate({
                scrollTop: $('.map-btn').offset().top-((offset.top/2)-30)},
                500);
        }
    });


}());