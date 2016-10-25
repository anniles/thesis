$(document).ready(function() {

    //map button for desctop
    $('.map-btn').on('click', function() {
        // var docPos = $(document).scrollTop();
        if( !($('.collapse').hasClass('in')) ) {
            $('.collapse').addClass('in');
            $('html,body').animate({
                scrollTop: $('.map-btn').offset().top-50},
                500);
            setTimeout(function() {
                $('#map').css('z-index', '1')
            }, 500);
        }else {
            $('#map').css('z-index', '-1')
            
            var offset = $('.map-btn').offset();

            $('.collapse').removeClass('in');
            $('html,body').animate({
                scrollTop: $('.map-btn').offset().top-(offset.top/2)},
            500);
        }
    });

    //hotels page filter button
    $('.filters-btn').on('click', function() {
        $('.filters-options').animate({
            height: 'toggle'
        });
    });



    //mobile and smaller screens query
    if ($(window).width() <= 940){  
        
        //hotel page header
        $('.page-hotel-price').removeAttr('self');
        $('.page-hotel-info').removeAttr('self');


        //map button for mobile
        $('.map-btn-mobile').on('click', function() {
            // var docPos = $(document).scrollTop();
            if( !($('.collapse').hasClass('in')) ) {
                $('.collapse').addClass('in');
                $('html,body').animate({
                    scrollTop: $('.map-btn-mobile').offset().top-50},
                    500);
                setTimeout(function() {
                    $('#map').css('z-index', '1')
                }, 500);
            }else {
                $('#map').css('z-index', '-1')
                
                var offset = $('.map-btn-mobile').offset();

                $('.collapse').removeClass('in');
                $('html,body').animate({
                    scrollTop: $('.map-btn-mobile').offset().top-(offset.top/2)},
                500);
            }
        });
    }
});


