jQuery(document).ready(function(){
    $(".slider").slider(
        {
            value: 50,
            min: 0,
            max: 100,
            step: 1,
            slide: function( event, ui ) {
                $( "#quality" ).val(ui.value);
            }
        }
    );
    $(".brightness").slider(
        {
            value: 0,
            min: -100,
            max: 100,
            step: 1,
            slide: function( event, ui ) {
                $( "#brightness" ).val(ui.value);
            }
        }
    );
    $(".contrast").slider(
        {
            value: 0,
            min: -100,
            max: 100,
            step: 1,
            slide: function( event, ui ) {
                $( "#contrast" ).val(ui.value);
            }
        }
    );
    $('input[type="checkbox"]').on('change', function() {
       $(this).siblings('input[type="checkbox"]').prop('checked', false);
    });
});