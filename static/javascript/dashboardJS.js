$(document).ready(function(){
    var data =  JSON.parse(localStorage.getItem('data'))
    $('#alerter').text(`Hello ${data.name} ${data.lname} ,Welcome Back !`)
    setTimeout(function(){
        $('#alerter').fadeOut('fast')
    }, 1000)
})

function changeActive(value) {
    $('#navbarNav ul li').find('a.nav-link.active').attr('class','nav-link')
    $('#'+value).attr('class', 'nav-link active')
}

$('#notifList').click(function(){
    $('#notifRedDot').show()
})

function showit(){
    $('#notifRedDot').show()
}