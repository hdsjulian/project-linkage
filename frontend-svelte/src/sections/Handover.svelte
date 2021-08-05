<script>
  import api from "../api"

  let getHandover = api.list("/handovers/1")
</script>

{#await getHandover}
  <p>Loading...</p>
{:then handover}
  <dl>
    <dt>Handover number</dt>
    <dd>{handover.id}</dd>
    <dt>For coin</dt>
    <dd>{handover.coin.id}</dd>
    <dt>Given from</dt>
    <dd>{handover.giver.name}</dd>
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
{:catch error}
  <p class="error"><b>Error</b> <small>{error.message}</small></p>
{/await}

<nav class="paging">
  <ul class="paging__list">
    <li class="previous"><a>Previous</a></li>
    <li class="next"><a>Afterwards</a></li>
  </ul>
</nav>
