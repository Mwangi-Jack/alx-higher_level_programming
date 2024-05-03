$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(response){
	console.log(response.results)
	const results = response.results
	results.forEach((result)=>{
		$('ul#list_movies').append(`<li>${result.title}</li`)
	})
})
