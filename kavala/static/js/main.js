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
                scrollTop: $('.map-btn').offset().top-((offset.top/2)-30)},
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
                    scrollTop: $('.map-btn-mobile').offset().top-((offset.top/2)+60)},
                500);
            }
        });


    }

    if ($(window).width() <= 700){  
        mobileNavOn();
    }

    $(window).on('resize',function(){
        if ($(window).width() <= 700){  
            mobileNavOn();
        }  else {
            mobileNavOff();
        }
    });

    //slick carousel for hotel images page
    $('.hotel-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        cssEase: 'linear',
        asNavFor: '.hotel-nav'
    });
    $('.hotel-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.hotel-slider',
        dots: false,
        arrows: false,
        infinite: true,
        centerMode: false,
        focusOnSelect: true,
        responsive: [
        {
          breakpoint: 500,
          settings: {
            slidesToShow: 3,
            }
        }]
    });

    //slick carousel for hotel room images
    $('.room-img-slider').slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 550,
            settings: {
                slidesToShow: 2,
                arrows: true,
            }
        }]
    });
    
    
});


// functions
function mobileNavOn() {

    $('nav').css('display', 'none');
    
    //open navigation menu
    $('.navigation-open').on('click', function() {
        $('nav').css({
            'display': '-webkit-box',
            'display': '-ms-flexbox',
            'display': 'flex'
        });
    });
    
    //close navigation menu
    $('.nav-close').on('click', function() {
        $('nav').fadeOut();
    });

    var menu = $('.navigation-open').offset().top;

    //sticky menu
    $(window).on('scroll', function() {
        if(($(window).scrollTop() - menu) >= 50) {
            $('.navigation-open').fadeIn().css({
                'background': 'rgba(0, 0, 0, .5)',
                'position': 'fixed',
                'width': '100%'
            })
        } else {
            $('.navigation-open').css({
                'background': 'none',
                'position': 'absolute',
                'width': 'initial'
            });

        }
    });
}

function mobileNavOff() {
 //open navigation menu
    $('.navigation-open').off('click');
    
    //close navigation menu
    $('.nav-close').off('click');

    $('nav').fadeIn();

    $(window).off('scroll');
}