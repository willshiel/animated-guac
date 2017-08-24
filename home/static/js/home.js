$( document ).ready(function() {

    $( "#pickError" ).hide();
    $( "#matchupError" ).hide();

    $( "#viewLockedPicks" ).click(function() {
        $ ( "#pickError" ).show();
    });

    $( "#viewLockedMatchup" ).click(function() {
        $ ( "#matchupError" ).show();
    });

});