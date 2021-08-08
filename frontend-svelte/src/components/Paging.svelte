<script>
  export let prevStep
  export let nextStep
</script>

<nav class="paging">
  <ul class="paging__list">
    <li><button on:click={prevStep} type="button">Previous</button></li>

    <li>
      <button on:click={nextStep} type="button" class="next">Afterwards</button>
    </li>
  </ul>
</nav>
