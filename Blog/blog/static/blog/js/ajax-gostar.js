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
            console.log(comentarios);
          });

        let botao = "<div id='gravar' class='d-flex p-2'>"
        + "\t<div style='margin-left: 10%;' class='p-2'>"
        + "\t<img style='float:left;' src='../{{post.autor.pic}}' class='rounded-circle' alt='perfil' width='40' height='40'>"
        + "\t</div>"
        + "\t<div class='p-2 comentario'><textarea autofocus style='width: 100%; background: transparent; border: none; font-size: 12px; + border-bottom: 1px solid grey;' type='text-area'></textarea>"
        + "\t<br>"
        + "\t<br><a id='btn-enviar-comentario' class='item-menu' type='button'>&#x1F5E3;&nbsp;Enviar</a>"
        + "\t</div>"
        + "</div>";
  
      $("#comentarios" + post_id).html(comentarios + botao);
      $("#comentarios" + post_id).toggle(300);
        
    });

}