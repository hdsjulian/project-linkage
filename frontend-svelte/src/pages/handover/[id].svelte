<script>
  import { url, params, afterPageLoad } from "@roxi/routify"
  import { dataset_dev } from "svelte/internal"
  import api from "../../api"
  let handover
  let id
  let lat
  let lon
  let timestamp
  let prevId
  let nextId
  let prevCoin
  let nextCoin

  let text
  let answer
  let question
  let prevLat = 0
  let prevLon = 0
  let markers = []
  let index = 0
  let isNew = new URLSearchParams(window.location.search).has("newHandover")

  function onClick(handover_id) {
    history.replaceState({}, null, `/handover/${handover_id}`)
  }

  $afterPageLoad(() => {
    id = parseInt($params.id, 10)
    console.log(process.env.FRONTEND_APP_API_URL)
    api.get(`/handovers/${id}`).then((res) => {
      console.log(res)
      handover = res.data?.handover
      myMap.setView([handover.lat, handover.lon], 10)
      timestamp = new Date(handover.timestamp * 1000).toLocaleDateString(
        "de-DE"
      )
      lat = handover.lat.toFixed(3)
      lon = handover.lon.toFixed(3)
      prevId = handover.prevId
      nextId = handover.nextId
      text = handover.text
      console.log(handover.coin)
      question = handover.coin.question
      answer = handover.answer
      api.get(`/coins/${handover.coinId}/handovers`).then((hl_res) => {
        let iterator = 0
        myMap.eachLayer((layer) => {
          if (iterator > 0) {
            layer.remove()
          }
          iterator += 1
        })
        for (const ho of hl_res) {
          markers.push(
            L.marker([ho.lat, ho.lon], { icon: mapMarker })
              .addTo(myMap)
              .on("click", () => onClick(ho.id, index))
          )
          if (prevLat != 0) {
            var polyLine = L.polyline(
              [
                [prevLat, prevLon],
                [ho.lat, ho.lon],
              ],
              { color: "red", weight: 5 }
            ).addTo(window.myMap)
          }
          index += 1
          prevLat = ho.lat
          prevLon = ho.lon
        }
        prevLat = 0
        prevLon = 0
      })
      api.get(`/handovers/${id}/coins`).then((res) => {
        nextCoin = res.data?.nextCoinHandoverId
        prevCoin = res.data?.prevCoinHandoverId
        console.log(nextCoin)
      })
    })
  })
</script>

{#if handover}
  <nav class="paging">
    <ul class="paging__list">
      <li class="previous">
        <a use:$url href={`/handover/${prevCoin}`}>Previous Coin</a>
      </li>
      <li class="next">
        <a use:$url href={`/handover/${nextCoin}`}>Next Coin</a>
      </li>
    </ul>
  </nav>

  {#if isNew == true}
    {#if handover.giver != null}
      <p>
        Thank you! {handover.recipient.name} is now all set to hand over this coin
        to another person! This coin, by the way, carries the id {handover.coin
          .id} and you can keep track of its path
        <a href="/coin/{handover.coin.id}">here</a>.
      </p>
    {:else}
      <p>
        Thank you! {handover.recipient.name} is now all set to hand over this coin
        to another person! This coin, by the way, carries the id {handover.coin
          .id} and you can keep track of its path
        <a href="/coin/{handover.oin.id}">here</a>.
      </p>
    {/if}
  {/if}
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
    {#if handover.giver == null}
      <dt class="fullwidth">Their Question:</dt>
      <dd class="fullwidth">{question}</dd>
    {:else}
      <dt class="fullwidth">Their answer to {question}</dt>
      <dd class="fullwidth">{answer}</dd>
      <dt class="fullwidth">What they had to say to each other</dt>
      <dd class="fullwidth">{text}</dd>
    {/if}
    
  </dl>
  {#if prevId !== nextId}
    <nav class="paging">
      <ul class="paging__list">
        {#if prevId < handover.id}
          <li class="previous">
            <a use:$url href={`/handover/${prevId}`}>Previous</a>
          </li>
        {:else}
          <li class="previous">
            <a use:$url href={`/handover/${prevId}`}>Last</a>
          </li>
        {/if}
        {#if nextId > handover.id}
          <li class="next">
            <a use:$url href={`/handover/${nextId}`}>Next</a>
          </li>
        {:else}
          <li class="next">
            <a use:$url href={`/handover/${nextId}`}>First</a>
          </li>{/if}
      </ul>
    </nav>
  {/if}
{/if}
