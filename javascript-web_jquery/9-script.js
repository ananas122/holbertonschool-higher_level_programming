// Make an AJAX GET request to the API URL
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const hello = data.hello;

  $('#hello').append(hello);
});