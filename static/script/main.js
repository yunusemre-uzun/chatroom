console.log('open');
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

};

setTimeout(refresh,3000);
