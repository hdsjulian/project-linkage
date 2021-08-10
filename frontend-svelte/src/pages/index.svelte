<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
  import { dataset_dev } from "svelte/internal";
  import api from "../api";
  let handover
  let id
  let lat
  let lon
  let timestamp
  let prevId
  let nextId
  let text
  let prevLat = 0
  let prevLon = 0
  function onClick(handover_id) { 
  history.replaceState({}, null, `/handover/${handover_id}`)
  
  }
  $afterPageLoad(() => {
    api.get(`/handovers`).then((res) => {
      for (const ho of res) {
        L.marker([ho.lat, ho.lon], {icon: mapMarker}).addTo(myMap).on('click', () => onClick(ho.id))
        prevLat = ho.lat
        prevLon = ho.lon
      }
      myMap.setView([prevLat, prevLon], 6)
    })
  })

</script>


<section class="about" id="about">
  <h4>Project linkage is an experiment about human trust</h4>
  <p>
    A number of initial participants received coins with an individual QR code on the back. They have five basic tasks:
  </p>
  <ul>
    <li>Hand this coin to a person they trust
    <li>Have a conversation about their mutual relationship
    <li>Scan the QR code and document the handover
    <li>Write a short text about their conversation for everyone to read
    <li>Request that the receiving person repeats these five steps
  </ul>
  <p>Thus, we create chains based on human trust. And tell our stories.</p>
</section>
