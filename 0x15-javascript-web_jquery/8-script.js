$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const x in data.results) {
    $('#list_movies').append('<l1>' + data.results[i].title + '</l1>);
  }
});
