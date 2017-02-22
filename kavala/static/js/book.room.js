(function() {
    "use strict";

    $(function() {
        var $no  = $('#_no_master');
        var $yes = $('#_yes_master');
        var $continue = $('._continue');
        var $form = $('form[name="hotel"]');

        checkValidation();

        $no.on('click', function() {
            $('#_from').remove();
            $form.submit();
        });

        // add hidden input gimme_car
        $yes.on('click', function() {
            $('<input />').attr('type', 'hidden')
                .attr('name', "from")
                .attr('value', "hotel")
                .attr('id', "_from")
                .appendTo($form);
            $form.submit();
        });

        // disable continue btn if no checkbox selected
        $form.change(checkValidation);

        function checkValidation () {
            if ($form.find(':checked').length) {
                $continue.prop('disabled', false);
            } else {
                $continue.prop('disabled', true);
            }
        }

        $continue.on('click', function() {
           if($(this).prop('disabled') === true) {
               alert('You have to select a room to continue');
           }
        });

    });

} ());
