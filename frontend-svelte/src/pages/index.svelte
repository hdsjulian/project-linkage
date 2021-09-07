<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
  import { dataset_dev } from "svelte/internal"
  import Rules from "rules.svelte"

  import api from "../api"
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
          layer.remove()
        }
        iterator += 1
      })
      for (const ho of res) {
        L.marker([ho.lat, ho.lon], { icon: mapMarker })
          .addTo(myMap)
          .on("click", () => onClick(ho.id))
        prevLat = ho.lat
        prevLon = ho.lon
      }
      myMap.setView([prevLat, prevLon], 6)
    })
  })
</script>

<Rules />
