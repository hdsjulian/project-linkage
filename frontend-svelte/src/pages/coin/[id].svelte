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


  $afterPageLoad(() => {
    id = parseInt($params.id, 10)
    api.get(`/coins/${id}`).then((res) => { 
      coin = res.data.coin
      handover = coin.handover
      travels = coin.travels
      recipientName = handover.recipient.name
      giverName = handover.giver.name
      lat = handover.lat
      lon = handover.lon
      console.log(coin)

    })
    prevId = id > 1 ? id - 1 : 1
    nextId = id + 1
  })
</script>

ID: {id}

<dl>
  <dt>Travels</dt>
  <dd>{travels}</dd>
  <dt>Currently held by</dt>
  <dd>{recipientName}</dd>
  <dt>Received from</dt>
  <dd>{giverName}</dd>
  <dt>Handed over on</dt>
  <dd>2021-08-31 14:56:17</dd>
  <dt>at Lon:Lat</dt>
  <dd>{lon}:{lat}</dd>
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
