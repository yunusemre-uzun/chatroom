console.log('open');
function refresh() {
    console.log("refresh");
    $.ajax({
        url: '/user/ilayda/chat',
        dataType : 'html',
        cache : true,
        timeout : 30000,
        success: function(data){
            $('#messages').html(data);
        }
    });

};

setTimeout(refresh,3000);
