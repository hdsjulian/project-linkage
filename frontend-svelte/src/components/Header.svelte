<script>
  import { url } from "@roxi/routify"

  let checked = false

  const toggleMenu = () => (checked = !checked)
</script>

<header class="page-header" id="page-header">
  <div class="page-menu menu">
    <div class="menu-toggle">
      <input
        on:click={toggleMenu}
        class="visually-hidden"
        id="menu-toggle"
        type="checkbox"
        {checked} />

      <label class="menu-toggle__hook" for="menu-toggle">
        <div class="menu-toggle__hook-icon">
          <svg class="icon--menu"><use xlink:href="#menu" /></svg>
          <svg class="icon--close"><use xlink:href="#close" /></svg>
        </div>
      </label>

      <div class="menu-toggle__object" id="menu">
        <!--include _page-search.pug -->
        <nav class="nav--main">
          <ol class="nav__list">
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/">About</a>
            </li>
<!--            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/coin">Coins</a>
            </li>
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/handover">Handovers</a>
            </li>
-->
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/profile">Profile</a>
            </li>
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/team">Team</a>
            </li>
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/legal">Legal</a>
            </li>
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/faq">FAQ</a>
            </li>
            <li class="nav__item">
              <a on:click={toggleMenu} use:$url href="/privacy">Privacy </a>
            </li>
          </ol>
        </nav>
      </div>
    </div>
  </div>
</header>
