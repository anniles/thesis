$(document).ready(function() {


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
        $('.page-rental-price').removeAttr('self');
        $('.page-rental-info').removeAttr('self');

    }

    if ($(window).width() <= 940){
        mobileNavOn();
    }

    $(window).on('resize',function(){
        if ($(window).width() <= 940){
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
    //slick carousel for rental images page
    $('.rental-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        cssEase: 'linear',
        asNavFor: '.rental-nav'
    });
    $('.rental-nav').slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        asNavFor: '.rental-slider',
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
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                arrows: true,
            }
        }]
    });

    //slick carousel for car rental images
    $('.rental-img-slider').slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
        {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                arrows: true,
            }
        }]
    });


    // header search booking
    $('ul.tabs li').click(function(){
        var tab_id = $(this).attr('data-tab');

        $('ul.tabs li').removeClass('current');
        $('.tab-content').removeClass('current');

        $(this).addClass('current');
        $("#"+tab_id).addClass('current');
    })


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