$(document).ready(function(){

  $('#id_season').change(function(){
    console.log($(this).val())
    var url_id = $(this).val()
      $.get('/farmstand/get_season_weeks/' + url_id, function(response){
          var split_response = response.split(',');
          for(i=0;i<split_response.length;i++)
          {
              console.log(split_response[i]);
              $('#id_week').append('<option value=' + i + '>' + split_response[i] + '</option>');
          }
      });
  });
});
