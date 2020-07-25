function createAccShow() {
    $('#signin').hide()
    $('#createAcc').show()
}

function signIn() {
    $('#createAcc').hide()
    $('#signin').show()
}

function register() {
    var json = {
        email: $('#inputEmailC').val(),
        name: $('#inputNameC').val(),
        lname: $('#inputLnameC').val(),
        dob: $('#inputDateC').val(),
        password: $('#inputPasswordC').val(),
    }
    $.ajax({
        type:"POST",
        url: "http://192.168.1.4:5000/register",
        contentType: 'application/json',
        data: JSON.stringify(json),
        success: function () { 
            console.log('DONE')
        }
    })
}

function login() {
    var json = {
        email: $('#inputEmail').val(),
        password: $('#inputPassword').val()
    }
    $.ajax({
        type:"POST",
        url:"http://192.168.1.4:5000/login",
        contentType: 'application/json',
        data: JSON.stringify(json),
        success: function (data) {  
            if(data === 'User Not found')
                $('#signin').append('<p id="notfound" style="color: red;">USER NOT FOUND</p>')
            else
            window.open('http://yoururl.com', '_blank');
        }
    })
    setTimeout(function(){
        $('#notfound').hide()
    },3000)
}