/////////////////////////////////////////////////////////////////////
// Copy of app/DAS_framework/js/map.js
//    TODO: cleanup (for ex: move entire DAS_framework to frontend)
/////////////////////////////////////////////////////////////////////

var mymap = L.map("map", {
  center: [51.505, -0.09],
  zoom: 13,
  zoomControl: false,
  attributionControl: true,
  accessToken:
    "pk.eyJ1IjoicHJvamVjdGxpbmthZ2UiLCJhIjoiY2tycGk0ejA2MmQ1cTJucnZiZTRsOXZlYyJ9.YkeSvM4CDDlz9dHlkc7Zuw",
})

new L.Control.Zoom({ position: "bottomleft" }).addTo(mymap)

//L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=//{accessToken}', {
//    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright"><abbr //title="OpenStreetMap">OSM</abbr></a> contributors, Imagery © <a href="https://www.mapbox.//com/">Mapbox</a>',
//    maxZoom: 18,
//    id: 'mapbox/streets-v11',
//    tileSize: 512,
//    zoomOffset: -1,
//    accessToken: 'pk.//eyJ1IjoicHJvamVjdGxpbmthZ2UiLCJhIjoiY2tycGk0ejA2MmQ1cTJucnZiZTRsOXZlYyJ9.//YkeSvM4CDDlz9dHlkc7Zuw'
//}).addTo(mymap);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(mymap)
