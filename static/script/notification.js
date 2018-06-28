function refresh() {
    $.ajax({
        url: '/user/notification/'+username,
        async: true,
        dataType : 'html',
        timeout : 30000,
        success: function(data){
            $('#popupcont').html(data);
        }
    }) 
}
setTimeout(refresh,5000);
// When the user clicks on <div>, close the popup
function hideFunction() {
    if(prev_message_count==new_messages){
        key=0;
    }
    else{
        key=1;
    }
    var popup = document.getElementById("popup");
    popup.classList.toggle("hide");
}