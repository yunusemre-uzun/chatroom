console.log('open1');

function refresh() {
    console.log("refresh1");
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

