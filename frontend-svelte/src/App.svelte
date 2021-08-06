<script>
  import { Router } from "@roxi/routify"
  import { routes } from "../.routify/routes"

  // import Button from "./Button.svelte";
  import AsyncExample from "./components/AsyncExample.svelte"

  import Article from "./components/Article.svelte"
</script>

<main>
  <div class="page__outer">
    <div class="page__inner">
      <main class="page-main">
        <Article>
          <Router {routes} />
          <AsyncExample />
        </Article>
      </main>
    </div>
  </div>
</main>
