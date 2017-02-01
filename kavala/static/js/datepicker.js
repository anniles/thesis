$( function() {
    var dateFormat = "yy-mm-dd",

    // dates for hotel
    checkin_hotel = $( "#checkin_hotel" )
    .datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        checkout_hotel.datepicker( "option", "minDate", getDate( this ) );
    }),

    checkout_hotel = $( "#checkout_hotel" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        checkin_hotel.datepicker( "option", "maxDate", getDate( this ) );
    });


    // dates for cars
    pickup_car = $( "#pickup_car" )
    .datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        dropoff_car.datepicker( "option", "minDate", getDate( this ) );
    }),

    dropoff_car = $( "#dropoff_car" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        pickup_car.datepicker( "option", "maxDate", getDate( this ) );
    });


    // dates for bikes
    pickup_bike = $( "#pickup_bike" )
    .datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        dropoff_bike.datepicker( "option", "minDate", getDate( this ) );
    }),

    dropoff_bike = $( "#dropoff_bike" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        pickup_bike.datepicker( "option", "maxDate", getDate( this ) );
    });


    // dates for packages
    checkin_packages = $( "#checkin_packages" )
    .datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        checkout_packages.datepicker( "option", "minDate", getDate( this ) );
    }),

    checkout_packages = $( "#checkout_packages" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 1,
        dateFormat: dateFormat
    })
    .on( "change", function() {
        checkin_packages.datepicker( "option", "maxDate", getDate( this ) );
    });


    function getDate( element ) {
        var date;
        try {
            date = $.datepicker.parseDate( dateFormat, element.value );
        } catch( error ) {
            date = null;
        }

        return date;
    }
} );