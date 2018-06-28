function refreshnotification() {
    $.ajax({
        url: '/user/notification/'+username,
        async: true,
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            $('#popupcont').html(data);
        }
    })
    setTimeout(refreshnotification,3000);
}
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("popup");
    popup.classList.toggle("hide");
}
$( document ).ready(function() {
    // addCookieTab();
    refreshnotification()
});
