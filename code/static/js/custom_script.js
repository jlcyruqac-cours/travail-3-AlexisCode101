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

// $(document).ready(function(){
//     $("#request_horoscope").click(function(){
//         $.ajax({
//             url : '/horoscope',
//             type : 'POST',
//             data : $('#horoscope_input').serialize(),
//             success: function(response){
// 				console.log(response);
// 			},
// 			error: function(error){
// 				console.log(error);
// 			}
//         });
//     });
// });

$(function() {
    $('#request_horoscope').bind('click', function() {
        $.getJSON('/horoscope', {
            last_name_input: $('input[name="last_name_input"]').val(),
            first_name_input: $('input[name="first_name_input"]').val(),
            birthday_date: $('input[name="birthday_date"]').val()
        }, function(data) {
            $("#astro_sign_id").text(data.result);
            console.log(data.result);
            console.log(data.result2);
        });
        return false;
    });
});