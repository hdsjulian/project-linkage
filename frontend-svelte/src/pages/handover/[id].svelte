<script>
    import { url, params, afterPageLoad } from "@roxi/routify"
    import { dataset_dev } from "svelte/internal";
    import api from "../../api";
    let handover
    let id
    let lat
    let lon

    $afterPageLoad(() => {
        id = parseInt($params.id, 10)
        api.get(`/handovers/${id}`).then((res) => { 
            handover = res.data?.handover
            myMap.setView([handover.lat, handover.lon], 10)
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
      <dd>2021-08-31 14:56:17</dd>
      <dt>at Lon:Lat</dt>
      <dd>{handover.lat}:{handover.lon}</dd>
      <dt>What they had to say to each other</dt>
      <dd>
        {handover.text}
      </dd>
    </dl>
{/if}
  <nav class="paging">
    <ul class="paging__list">
      <li class="previous"><a>Previous</a></li>
      <li class="next"><a>Afterwards</a></li>
    </ul>
  </nav>
  