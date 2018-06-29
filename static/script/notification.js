function refreshnotification() {
    $.ajax({
        url: '/user/notification/'+username,
        async: true,
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            $('#popup_text').html(data);
        }
    })
}
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("popup");
    popup.classList.toggle("hide");
}
setInterval(refreshnotification,3000);
/*
$( document ).ready(function() {
    // addCookieTab();
    refreshnotification()
});
*/
