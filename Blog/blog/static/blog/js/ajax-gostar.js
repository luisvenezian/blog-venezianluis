$( document ).ready(function() {
    $('.gostar').click(function(){
        var postid;
        postid = $(this).attr("data-postid");

        //alert("post: " + postid);
        $.get('/gostar/', {postid: postid}, function(data){
            data = JSON.parse(data);
            $("#" + postid).find("#gostaram").html(data.gostaram);
            if (data.classe == ""){
                $("#" + postid).find("#gostar").removeClass("gostou")
            }
            else {
                $("#" + postid).find("#gostar").addClass(data.classe)
            }
            
            ///$('#likes').hide();  
        });
    });
});