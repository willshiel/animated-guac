$( document ).ready(function() {

    $( "#scoring-popup" ).click(function () {

        $( "#scoring-modal" ).show();

    });

    $( "#modal-close" ).click(function() {
        $( "#scoring-modal" ).hide();
    });

    /**
     * disables the margin field for a selected draw
     */
    $( ".picks" ).each(function () {
        $( this ).change(function () {
            var selectedText = $ ( this ).find(":selected").text();
            var selectedMargin  = $( this ).closest("td").next().find("input");
            if (selectedText == "Draw") {
                selectedMargin.val(0);
            }
            else {
                selectedMargin.val(undefined);
            }
        });
    });

});