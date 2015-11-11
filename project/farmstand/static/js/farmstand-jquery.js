$(document).ready(function(){

  $('#id_season').change(function(){
    console.log($(this).val())
    var url_id = $(this).val()
      $.get('/farmstand/get_season_weeks/' + url_id, function(response){
          $('#id_week').append(response);
          console.log(response)
      });
  });
});
