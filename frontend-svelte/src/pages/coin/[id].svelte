<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
import { dataset_dev } from "svelte/internal";
import api from "../../api";

  let id
  let coin
  let prevId
  let nextId
  let handover
  let recipientName
  let giverName
  let travels
  let lat
  let lon
  let lon2
  let timestamp
  let text
  let handoverList

  function onClick(handover_id) { 
   history.replaceState({}, null, `/handover/{handover_id}`)
   
  }

  $afterPageLoad(() => {
    id = parseInt($params.id, 10)
    api.get(`/coins/${id}`).then((res) => { 
      coin = res.data?.coin
      handover = coin?.handover
      text = handover?.text
      console.log(handover)
      travels = coin?.travels
      recipientName = handover?.recipient.name
      giverName = handover.giver?.name
      timestamp = new Date(handover.timestamp * 1000).toLocaleDateString("de-DE")
      lat = handover.lat.toFixed(4)
      lon = handover.lon.toFixed(4)
      console.log(lat)
      myMap.setView([lat, lon], 10)
      api.get(`/coins/${id}/handovers`).then((hl_res) => {
        let polyFill = hl_res?.map((val) => [val.lat, val.lon])
        console.log(polyFill)
        console.log(polyFill[0])
        for (const line of hl_res) { 
          L.marker([line.lat, line.lon], {icon: mapMarker}).addTo(myMap).on('click', onClick(line.id))

        }
        var polyLine = L.polyline([polyFill[0], polyFill[2]], {color:'red', weight: 5}).addTo(window.myMap)
      })
    })
      

      //var polygon = L.polygon(polyFill).addTo(window.myMap);



    prevId = id > 1 ? id - 1 : 1
    nextId = id + 1
  })

</script>
{#if coin}
ID: {id}

<dl>
  <dt>Traveless</dt>
  <dd>{travels}</dd>
  <dt>Currently held by</dt>
  <dd>{recipientName}</dd>
  {#if giverName != null }
  <dt>Received from</dt>
  <dd>{giverName}</dd>
  {/if}
  <dt>Handed over on</dt>
  <dd>{timestamp}</dd>
  <dt>at Lat:Lon</dt>
  <dd>{lat}:{lon}</dd>
  {#if text != ""}
  <dt class = "fullwidth">What they had to say to each other</dt>
  <dd class = "fullwidth">{text}</dd>
  {/if}
</dl>
<nav class="paging">
  <ul class="paging__list">
    <li class="previous">
      <a use:$url href={`/coin/${prevId}`}>Previous</a>
    </li>

    <li class="next">
      <a use:$url href={`/coin/${nextId}`}>Afterwards</a>
    </li>
  </ul>
</nav>
{:else}
  <p>Coin not found!</p>
{/if}

