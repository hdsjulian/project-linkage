var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicHJvamVjdGxpbmthZ2UiLCJhIjoiY2tycGk0ejA2MmQ1cTJucnZiZTRsOXZlYyJ9.YkeSvM4CDDlz9dHlkc7Zuw'
}).addTo(mymap);
console.log('fosdo');

