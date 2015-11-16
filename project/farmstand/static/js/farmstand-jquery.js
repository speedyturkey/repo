$(document).ready(function(){

  $('#id_season').change(function(){
    $('#id_week').empty()
    var url_id = $(this).val()
      $.get('/farmstand/get_season_weeks/' + url_id, function(response){
        var obj = jQuery.parseJSON(response)
        $('#id_week').append('<option value="">--Select a week--</option')
        for (var i=0; i < obj.length; i++) {
            $('#id_week').append('<option value=' + obj[i].id + '>' + obj[i].number + '</option>');
        }
      });
  });//end season change function
  
  $('#id_week').change(function(){
    // Upon change in week selection,
    // uncheck all currently checked checkboxes.
    $.each($('input:checked'), function(){
      $(this).removeAttr("checked")
    });
    var url_id = $(this).val()
    $.get('/farmstand/get_week_products/' + url_id, function(response){
      // If there are week_product records associated with
      // the selected week, pre-populate checkboxes.
      if(response.length > 0){
          array = response.split(',');
          for (var i=0; i < array.length; i++) {
            console.log(array[i])
            $("input[value=" + array[i] + "]").prop("checked","true");
          }
        }
      else {}
    });
  });//end week change function

});
