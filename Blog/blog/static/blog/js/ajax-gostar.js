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

function ver_comentario(post_id){
    
    var postid = post_id, comentarios = "";

    $.get('/comentarios/', {postid: postid}, function(data){
        data = JSON.parse(data);
        
        $.each(data, function(i, obj) {
            
            comentarios += "<div id='comentario1' class='d-flex p-2'>"
                + "\t<div style='margin-left: 10%;' class='p-2'>"
                + "\t<img style='float:left;' src='../"+obj.pic+"' class='rounded-circle' alt='perfil' width='40' height='40'>"
                + "\t</div>"
                + "\t<div class='p-2 comentario'><font style='color: grey; font-size: 10px;'>[Jul 27 8:38 PM] &bull;</font> "+obj.comentario+" </div>" 
            + "</div>"; 
          });
  
          $("#comentarios" + post_id).toggle(300);
          $("#comentar" + post_id).removeAttr("style");
      $("#comentarios" + post_id).html(comentarios);
     
/*
      if(!$("#comentarios" + post_id)[0].style.display == "none"){
        $("#comentar" + post_id).css('display', 'none');
      }
      else i
      if (!css){
        
      }
      else {
        $(comentario).css('display', 'none');
      }
      */
    
      
    });

}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function comentar(post_id){
    var comentario = $('#comentario' + post_id).val();

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    $.ajax({
        method: "POST",
        url: "/comentar/",
        data: { comentario: comentario, post_id: post_id}
       })

    location.reload();


    
}