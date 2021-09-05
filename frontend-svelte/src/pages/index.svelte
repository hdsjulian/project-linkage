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
  if (document.getElementById("mapwrapper").classList.contains("is-hidden")) {
    document.getElementById("article").classList.remove("fullwidth")
    document.getElementById("mapwrapper").classList.remove("is-hidden")
  }
    api.get(`/handovers`).then((res) => {
      let iterator = 0
      myMap.eachLayer((layer) => {
          if (iterator > 1) { 
              layer.remove();
          }
          iterator +=1
      });
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
  <h4>Project Linkage is an experiment about human trust</h4>
  <strong>IMPORTANT!</strong> this is an art project. We will never abuse any entered data for commercial purposes. 
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
  <p>Thus, we create chains based on human trust. And tell our stories. Click on a map icon to check them out!</p>
</section>
