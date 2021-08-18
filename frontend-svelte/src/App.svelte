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
              <header class="article__header">
        <h1 class="a11y">Projects Linkage</h1>
          <div class="figure logo">
        <img alt="Project Linkage logo" src="/image/logo/project-linkage.svg" />
        </div>
      </header>
          <Router {routes} />
          
        </Article>
      </main>
    </div>
  </div>
</main>
