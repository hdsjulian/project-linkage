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
    <dd>Erica</dd>
    <dt>Given to</dt>
    <dd>Anna</dd>
    <dt>Handed over on</dt>
    <dd>2021-08-31 14:56:17</dd>
    <dt>at Lon:Lat</dt>
    <dd>55.458:25.873</dd>
    <dt>What they had to say to each other</dt>
    <dd>
      This is an experiment about trust. We have been friends from age six. We
      trust each other and love each other and will be there for each other
      however long our life will go, in whatever situation we are. We were
      bridesmaids at our weddings and we will be buried together in the same
      grave because besties
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
