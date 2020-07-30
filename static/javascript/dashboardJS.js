$(document).ready(function(){
    
    alert(data.name)
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

function logout() {
    window.open("http://192.168.1.6:5000/logout","_self")
}