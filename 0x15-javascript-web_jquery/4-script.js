$(document).ready(function() {
	const prevColor = $("#toggle_header").attr("class")
	$("#toggle_header").click(()=>{
		$("header").toggleClass("red green")
	})
})
