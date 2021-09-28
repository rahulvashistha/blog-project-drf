$(document).ready(function(){
  $("#postcomment").on('click',function(){
    var comment=$("#commenttext").val()
    var postsno=$("#postSno").val()
    //let token =$("#csrf").val();
    //var commentsno=$("#parentSno").val()

    console.log(comment, postsno)

    //Ajax
    $.ajax({
      url:"post-comment",
      type:"POST",
      data:{
          'comment': comment,
          'postsno': postsno,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
          //'_csrf': token
      },
      dataType:'json',
      beforeSend:function(){
          $("#postcomment").addClass('disabled').text('Commenting')
      },
      sucess:function(data){
          console.log(data)
          if(data.bool==true){
            $("#commenttext").val('')
            //Append Element
            var html='<div class="card my-3 animate__animated animate__bounce">\
              <div class="card-body">\
              <b>{{request.user}}</b><span class="badge bg-secondary">{{comment.timeStamp | naturaltime}}</span>\
              <div>'+comment+'</div>\
              </div>\
              </div>'
          $(".comment-wrapper").append(html)
          }
          $("#postcomment").removeClass('disabled').text('Comment')
      }
    })
  })
})

/*$(document).ready(function(){
  $("#postcomment").on('click',function(){
    //make xhr object
    const xhttp = new XMLHttpRequest();

    //on result
    xhttp.onload = function() {
        if (this.status === 200) {
            console.log(this.responseText);
        } else {
            console.log("Error Occured")
        }
    }
    
    //on progress
    xhttp.onprogress = function() {
      $("#postcomment").addClass('disabled').text('Commenting')
    }

    //open the object
    xhttp.open('POST', '/blog/PostComment');
    xhttp.getResponseHeader('Content-type', 'application/json');

    //on send request
    params = `{"name":"t512","salary":"12743","age":"273"}`;
    xhttp.send(params);
}
*/