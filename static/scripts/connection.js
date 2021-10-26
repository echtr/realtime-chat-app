// github.com/echtr
$(document).ready(function(){
    $("#post_form").submit(function(event){
        event.preventDefault();
        var $form=$(this);
        $.ajax({
            type: "POST",
            url: $form.attr("action"),
            dataType: "json",
            data: $form.serialize(),
            async: false,
            success: function(data){
                console.log(data);
            },
            error: function(error){
                console.log(error);
            }
        });
        $("#message").val("");
    });
});