function refresh111() {
    $.ajax({
        url: '/user/ajaxFriends/'+username,
        async: true,
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            //console.log(data);
            $('#jj').html(data);
        }
    });
    console.log("refresh friendzone");
    setTimeout(refresh111,3000);
}
// When the user clicks on <div>, open the popup
function myFunction() {
    var popup = document.getElementById("myPopup");
   /*popup.classList.toggle("hide");*/
}
//setTimeout(myFunction, 0);

// Script to open and close sidebar
function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}
$( document ).ready(function() {
    // addCookieTab();
    refresh111()
});
