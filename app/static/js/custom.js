$(document).ready(function(){
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

    var jcrop_api;

    $('#width').val($("#target").height());
    $('#height').val($("#target").width());
    $('#target').Jcrop({
      onChange:   showCoords,
      onSelect:   showCoords,
      onRelease:  clearCoords
    },function(){
      jcrop_api = this;
    });

    $('#coords').on('change','input',function(e){
      var x1 = $('#x1').val(),
          x2 = $('#x2').val(),
          y1 = $('#y1').val(),
          y2 = $('#y2').val();
      jcrop_api.setSelect([x1,y1,x2,y2]);
    });
    function showCoords(c)
  {
    $('#x1').val(c.x);
    $('#y1').val(c.y);
    $('#x2').val(c.x2);
    $('#y2').val(c.y2);

  };
});