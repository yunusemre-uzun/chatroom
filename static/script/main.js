console.log('open');
//window.location.href = window.location.protocol +'//'+ window.location.host + window.location.pathname;
function refresh() {
    console.log("refresh");
    $.ajax({
        url: '',
        dataType : 'html',
        timeout : 30000,
        success: function(data){

            $('#messages').html(data);
        }
    });

}
setTimeout(refresh,2000);

