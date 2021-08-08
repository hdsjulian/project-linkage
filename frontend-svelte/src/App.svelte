<script>
  import { Router } from "@roxi/routify"
  import { routes } from "../.routify/routes"
  import Map from "./components/Map.svelte"

  // import Button from "./Button.svelte";
  import AsyncExample from "./components/AsyncExample.svelte"

  import Article from "./components/Article.svelte"
</script>

<Map />

<main>
  <div class="page__outer">
    <div class="page__inner">
      <main class="page-main">
        <Article>
          <Router {routes} />
          
        </Article>
      </main>
    </div>
  </div>
</main>
