<script>
  import { onMount } from "svelte"
  import L from "leaflet"
  import "leaflet/dist/leaflet.css"

  import { LEAFLET_ACCESS_TOKEN } from "../constants"

  let map

  onMount(async () => {
    map = L.map("map", {
      center: [51.505, -0.09],
      zoom: 19,
      zoomControl: false,
      attributionControl: true,
      accessToken: LEAFLET_ACCESS_TOKEN,
    })

    new L.Control.Zoom({ position: "bottomleft" }).addTo(map)

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map)
    window.myMap = map
    var mapMarker = L.icon({
      iconUrl: '/image/map/pin.svg', 
      iconSize: [40, 40], 
      iconAnchor: [20,20], 
    })
    window.mapMarker = mapMarker

  })

  // Example function that interacts with the map:
  const unZoom = () => map.setView([0, 0], 0)
</script>

<figure id="map" style="z-index: 0" />

<!-- Example button to interact with the map -->
<button on:click={unZoom}>unZoom</button>

<!-- Throwaway style, just for the example -->
<style>
  button {
    position: absolute;
    top: 0;
    left: 50%;
    z-index: 100;
  }
</style>
