<script>
  import Article from "../components/Article.svelte"
  import BurgerSvg from "../components/Burger.svg.svelte"
  import PageHeader from "../components/PageHeader.svelte"
  import Map from "../components/Map.svelte"
</script>

<Map />

<BurgerSvg />

<main>
  <div class="page__outer">
    <div class="page__inner">
      <PageHeader />

      <main class="page-main">
        <Article>
          <header class="article__header">
            <h1 class="a11y">Projects Linkage</h1>

            <div class="figure logo">
              <img
                alt="Project Linkage logo"
                src="/image/logo/project-linkage.svg" />
            </div>
          </header>

          <slot />
        </Article>
      </main>
    </div>
  </div>
</main>
