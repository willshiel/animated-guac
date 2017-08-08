$( document ).ready(function() {

    $( "#scoring-popup" ).click(function () {

        $( "#scoring-modal" ).show();

    });

    $( "#modal-close" ).click(function() {
        $( "#scoring-modal" ).hide();
    });

});