alert("who are you")
$(document).ready(function(){
	$("button").click(function(){
		$.ajax(
		{
		    url:"http://localhost:8080/test",
		    type:'GET',
		    success:function(data)
		    {
		    $('#div1').html(data)
		    }
		}
		);
	});
});