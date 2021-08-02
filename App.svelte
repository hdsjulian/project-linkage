<script>
  // import Button from "./Button.svelte";
  import Article from "/components/Article.svelte"
  import BurgerSvg from "/components/Burger.svg.svelte"
  import Header from "/components/Header.svelte"
  import Map from "/components/Map.svelte"

  import About from "/sections/About.svelte"
  import Coin from "/sections/Coin.svelte"
  import Contact from "/sections/Contact.svelte"
  import Legal from "/sections/Legal.svelte"
  import Privacy from "/sections/Privacy.svelte"
  import Profile from "/sections/Profile.svelte"
</script>

<main>
  <BurgerSvg />
  <Header />

  <div class="page__outer">
    <div class="page__inner">
      <main class="page-main">
        <Map />

        <Article>
          <section class="contact" id="contact">
            <Contact />
          </section>

          <section class="legal" id="legal">
            <Legal />
          </section>

          <section class="privacy legal" id="privacy">
            <Privacy />
          </section>

          <section class="profile" id="profile">
            <Profile />
          </section>

          <section class="coin" id="coin">
            <Coin />
          </section>

          <section class="about" id="about">
            <About />
          </section>
        </Article>
      </main>
    </div>
  </div>
</main>
