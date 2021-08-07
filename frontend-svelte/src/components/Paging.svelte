<script>
  export let prevStep
  export let nextStep
</script>

<nav class="paging">
  <ul class="paging__list">
    <li><button type="button" on:click={prevStep}>Previous</button></li>
    <li><button type="button" on:click={nextStep}>Afterwards</button></li>
  </ul>
</nav>
