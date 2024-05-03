$(document).ready(()=>{
	$('input#btn_translate').on('click', ()=>{
		lang = $('input#language_code').val();
		$.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, function(response){
			$('div#hello').replaceWith(`<div id="hello">${response.hello}</div>`)
		})
	})

})
