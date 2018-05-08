document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelectorAll('#map').length > 0)
  {
    if (document.querySelector('html').lang)
      lang = document.querySelector('html').lang;
    else
      lang = 'en';

    var js_file = document.createElement('script');
    var js_file2 = document.createElement('script');
    js_file.type = 'text/javascript';
    js_file2.type = 'text/javascript';
    js_file.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBNeETj59ymLhoiZZdKb7rHIO7624slYZU&callback=initMap&language=' + lang;
    js_file2.src = 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js';
    document.getElementsByTagName('head')[0].appendChild(js_file);
    document.getElementsByTagName('head')[0].appendChild(js_file2);
  }
});

var map;

function initMap()
{
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 1
  });



}

var markers;
var bounds;

function plotMarkers(m)
{
  markers = [];
  bounds = new google.maps.LatLngBounds();

  m.forEach(function (marker) {
    var position = new google.maps.LatLng(marker.lat, marker.lng);

    markers.push(
      new google.maps.Marker({
        position: position,
        map: map,
        animation: google.maps.Animation.DROP
      })
    );

    bounds.extend(position);
  });

  map.fitBounds(bounds);
}

$(document).ready(function() {

  $("#search").click(function() {
    var search = $.get("/getGame/");
    search.done(function(data) {
      loadPlaces(data)
    });
  });

  function loadPlaces(string){
      var obj = jQuery.parseJSON(string);

    jQuery.each(obj, function() {
      search(this.place, this.tweet, this.sentiment)

});

  }

  var markers = []
  var markers2 = []

  function search(j, tweet, sent){
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+j.type+'+'+j.name+'+'+j.country+'&key=AIzaSyBNeETj59ymLhoiZZdKb7rHIO7624slYZU'
    $.getJSON(url, function(data) {
      pos=data.results[0].geometry.location
    var obj = [tweet,sent,pos]
    console.log(obj)

    markers.push(data.results[0].geometry.location)
    newMark(obj);
});
  }

  function newMark(m) {
    var position = new google.maps.LatLng(m[2].lat, m[2].lng);

    new google.maps.Marker({
      title: m[1]+" "+m[0],
      position: position,
      map: map,
      animation: google.maps.Animation.DROP
    });

  }



});
