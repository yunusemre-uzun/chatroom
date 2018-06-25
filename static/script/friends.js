console.log('open2');

function refresh() {
    console.log("refresh");
    $.ajax({
        url: '',
        dataType : 'html',
        timeout : 30000,
        success: function(data){

            $('#friends').html(data);
        }
    });

}
setTimeout(refresh,5000);
