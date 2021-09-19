$(document).ready(function(){
    $('#regEmail').keyup(function(){
        var data = $("#regform").serialize()
        $.ajax({
            method: "POST",
            url: "/register",
            data: data
        })
        .done(function(res){
            $('#emailMsg').html(res)
        })
    })
});