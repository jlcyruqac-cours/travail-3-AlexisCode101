// Used for datepicker
$( "#birthday_date_input" ).datepicker();

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
        last_name_input = $('#last_name_input').val();
        first_name_input = $('#first_name_input').val();
        birthday_date_input = $('#birthday_date_input').val();
        $.ajax({
            url : '/horoscope',
            type : 'POST',
            data : {
                'last_name_input': last_name_input,
                'first_name_input': first_name_input,
                'birthday_date': birthday_date_input
            },
            success: function(result){
				// $('#horoscope_display').text(result)
                $(this).html(result)
			},
			error: function(error){
				console.log(error);
			}
        });
    });
});

// $(function() {
//     $('#request_horoscope').bind('click', function() {
//         $.getJSON('/horoscope', {
//             last_name_input: $('input[name="last_name_input"]').val(),
//             first_name_input: $('input[name="first_name_input"]').val(),
//             birthday_date: $('input[name="birthday_date"]').val()
//         }, function(data) {
//             $("#astro_sign_id").text(data.result);
//             console.log(data.result);
//             console.log(data.result2);
//         });
//         return false;
//     });
// });