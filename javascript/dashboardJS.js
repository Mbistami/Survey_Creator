$(document).ready(function(){
    var data =  JSON.parse(localStorage.getItem('data'))
    $('#alerter').text(`Hello ${data.name} ${data.lname} ,Welcome Back !`)
    setTimeout(function(){
        $('#alerter').fadeOut('fast')
    }, 1000)
})