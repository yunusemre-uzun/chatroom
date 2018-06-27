function refresh123() {
    $.ajax({
        url: '/user/notification/'+username,
        async: true,
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            //console.log(data);
            $('#popup').html(data);
        }
    });
    console.log("refresh notification");

}
setTimeout(refresh123,3000);
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("popup");
    popup.classList.toggle("hide");
}
