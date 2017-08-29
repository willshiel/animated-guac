$( document ).ready(function() {

    $( "#pickError" ).hide();
    $( "#matchupError" ).hide();
    $( "#hasNotPicked" ).hide();

    $( "#viewLockedPicks" ).click(function() {
        $ ( "#pickError" ).show();
    });

    $( "#viewLockedMatchup" ).click(function() {
        $ ( "#matchupError" ).show();
    });

    $( "#viewMatchupWithoutPicking" ).click(function() {
        $ ( "#hasNotPicked" ).show();
    })
});