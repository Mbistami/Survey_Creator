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
var HelloUser = new String();
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
            if(data.msg === 'Success')
            {
                localStorage.setItem('data', JSON.stringify(data))
                window.open("../html/dashboard.html","_self")
            }
            else
                $('#signin').append('<p id="notfound" style="color: red;">USER NOT FOUND</p>')
        }
    })
    setTimeout(function(){
        $('#notfound').hide()
    },3000)
}