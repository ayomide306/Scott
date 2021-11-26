$(document).on('submit','.commentbox1', function(e){
    e.preventDefault();
	$.ajax({
		type:"POST",
		url:"{% url 'post:comment' %}",
		data:{
			postid:$("#postid").val(),
			said:$("#said").val(),
			csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
		},
		success:function(data){
		//	if document.querySelector(".body").innerHTML == data;
			if (data == "saved"){
			    alert("you commented on this post");
			}
			else{
			   alert("sorry you have to be logged in to like this post");
			}
			//document.querySelector(".title").value += "Hive";
		}
	});
});

