// Used for datepicker
$( "#date" ).datepicker();

// Used to display horoscope using AJAX
// $('a#request_horoscope').bind('click', function() {
//     $.getJSON('/horoscope', {
//         a: $('input[name="a"]').val(),
//         b: $('input[name="b"]').val()
//     }, function(data) {
//         $("#result").text(data.result);
//     });
//     return false;
// });

$(document).ready(function(){
    $("#request_horoscope").click(function(){
        $.ajax({
            url : '/horoscope',
            type : 'POST',
            data : $('#horoscope_input').serialize(),
            success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
        });
    });
});