$(document).ready(function(){

  //console.log({{ form.Season.id }})
  $('#id_season').change(function(){
    console.log($(this).val())
  });
  $('#id_season').change(function(){
    var url_id = $(this).val()
    //var url = '{% url get_season_weeks 9999 %}'.replace(9999, $(this).val())
      $.get('/farmstand/get_season_weeks/' + url_id, function(data){
          $('#id_week').html(data);
      });
    //$('#weeks').load("home.html");
    //$('#weeks').load('{% url get_season_weeks %}',{'season': $(this).val()});
      console.log("Get weeks attempted.")
  });

  $('#btn').click(function(){
    alert("You clicked the button.")
    console.log('Button clicked!');
  });
  console.log('foo');
});
