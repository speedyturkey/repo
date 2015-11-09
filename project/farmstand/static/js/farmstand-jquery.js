$(document).ready(function(){
  console.log({{ form.Season.id }})
  $('# {{ form.Season.id }} ').change(function(){
    $('#weeks').load('{% url get_season_weeks %}',
      {season: $(this).value()});
      console.log("Get weeks attempted.")
  });

  $('#btn').click(function(){
    alert("You clicked the button.")
    console.log('Button clicked!');
  });
  console.log('foo');
});
