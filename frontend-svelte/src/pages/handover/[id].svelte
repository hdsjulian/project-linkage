<script>
    import { url, params, afterPageLoad } from "@roxi/routify"
    import { dataset_dev } from "svelte/internal";
    import api from "../../api";
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
    let markers = []
    let index = 0

  function onClick(handover_id) { 

   history.replaceState({}, null, `/handover/${handover_id}`)
     
  }

    $afterPageLoad(() => {
        id = parseInt($params.id, 10)
        api.get(`/handovers/${id}`).then((res) => { 
            handover = res.data?.handover
            myMap.setView([handover.lat, handover.lon], 10)
            timestamp = new Date(handover.timestamp * 1000).toLocaleDateString("de-DE")
            lat = handover.lat
            lon = handover.lon
            prevId = handover.prevId
            nextId = handover.nextId
            text = handover.text
            console.log(handover)
            api.get(`/coins/${handover.coinId}/handovers`).then((hl_res) => {
                let iterator = 0
                myMap.eachLayer((layer) => {
                    if (iterator > 0) {
                        console.log("iterator "+iterator) 
                        console.log(layer)
                        layer.remove();
                    }
                    iterator +=1
                });
                for (const ho of hl_res) { 
                    markers.push(L.marker([ho.lat, ho.lon], {icon: mapMarker}).addTo(myMap).on('click', () => onClick(ho.id, index)))
                    if (prevLat != 0) {
                        console.log ("poly line "+prevLat+" prevLon "+prevLon+" holat "+ho.lat+" holon "+ho.lon)
                        var polyLine = L.polyline([[prevLat, prevLon], [ho.lat, ho.lon]], {color:'red', weight: 5}).addTo(window.myMap)
                    }
                    index +=1 
                    prevLat = ho.lat
                    prevLon = ho.lon

                }
                prevLat = 0;
                prevLon = 0;
            })
            console.log(markers)
        })
    })
</script>
{#if handover}
    <dl>
      <dt>Handover number</dt>
      <dd>{handover.id}</dd>
      <dt>For coin</dt>
      <dd>{handover.coin.id}</dd>
      {#if handover.giver != null}
      <dt>Given from</dt>
      <dd>{handover.giver.name}</dd>
      {/if}
      <dt>Given to</dt>
      <dd>{handover.recipient.name}</dd>
      <dt>Handed over on</dt>
      <dd>{timestamp}</dd>
      <dt>at Lon:Lat</dt>
      <dd>{lat}:{lon}</dd>
      <dt class = "fullwidth">What they had to say to each other</dt>
      <dd class = "fullwidth">{text}</dd>
    </dl>

  <nav class="paging">
    <ul class="paging__list">
      {#if prevId < handover.id}
      <li class="previous"><a use:$url href={`/handover/${prevId}`}>Previous</a></li>
      {:else}
      <li class="previous"><a use:$url href={`/handover/${prevId}`}>Last</a></li>      
      {/if}
      {#if nextId > handover.id}
      <li class="next"><a use:$url href={`/handover/${nextId}`}>Next</a></li>
      {:else}
      <li class="next"><a use:$url href={`/handover/${nextId}`}>First</a>
      {/if}
      
    </ul>
  </nav>
  {/if}