// github.com/echtr
$(document).ready(function(){
    var run = window.setInterval(function(){
        $.ajax({
            type: "GET",
            url: "get_datas",
            dataType: "html",
            success:function(response){
                $("#messages").html(response);
            }
        });
    },1000);
});