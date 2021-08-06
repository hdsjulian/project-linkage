<script>
  import { url, params, afterPageLoad } from "@roxi/routify"

  let id
  let prevId
  let nextId

  $afterPageLoad(() => {
    id = parseInt($params.id, 10)
    prevId = id > 1 ? id - 1 : 1
    nextId = id + 1
  })
</script>

ID: {id}

<dl>
  <dt>Travels</dt>
  <dd>6</dd>
  <dt>Currently held by</dt>
  <dd>Erica</dd>
  <dt>Received from</dt>
  <dd>Anna</dd>
  <dt>Handed over on</dt>
  <dd>2021-08-31 14:56:17</dd>
  <dt>at Lon:Lat</dt>
  <dd>55.458:25.873</dd>
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
