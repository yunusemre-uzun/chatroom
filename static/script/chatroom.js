function refresh() {
        console.log("refresh1");
        $.ajax({
            url: '/user/chatroom/'+username+'/'+receiver ,
            dataType : 'html',
            timeout : 30000,
            success: function(data){
                $('#messageList').html(data);
            }
        });
    }
setInterval(refresh,2000);




