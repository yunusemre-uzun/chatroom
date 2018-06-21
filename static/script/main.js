console.log('open');
//window.location.href = window.location.protocol +'//'+ window.location.host + window.location.pathname;
function refresh() {
    console.log("refresh");
    $.ajax({
        url: '',
        dataType : 'html',
        cache : false,
        timeout : 30000,
        success: function(data){
            $('#messages').html(data);
        }
    });

};
//setTimeout('window.location.href = window.location.protocol +\'//\'+ window.location.host + window.location.pathname',3000)
setTimeout(refresh,3000);
