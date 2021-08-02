<header class="page-header" id="page-header">
  <div class="page-menu menu">
    <div class="menu-toggle">
      <input class="visually-hidden" id="menu-toggle" type="checkbox" />

      <label class="menu-toggle__hook" for="menu-toggle">
        <div class="menu-toggle__hook-icon">
          <svg class="icon--menu">
            <use xlink:href="#menu" />
          </svg>
        </div>
      </label>

      <div class="menu-toggle__object" id="menu">
        <!--include _page-search.pug -->
        <nav class="nav--main">
          <ol class="nav__list">
            <li class="nav__item"><a href="#about">About</a></li>
            <li class="nav__item"><a href="#coin">Coins</a></li>
            <li class="nav__item"><a href="#profile">Profile</a></li>
            <li class="nav__item"><a href="#contact">Contact</a></li>
            <li class="nav__item"><a href="#legal">Legal</a></li>
            <li class="nav__item"><a href="#privacy">Privacy </a></li>
          </ol>
        </nav>
      </div>
    </div>
  </div>

  <script>
    var navigating = document.getElementsByClassName("nav__item")
    var hidemenu = function () {
      document.getElementById("menu-toggle").checked = false
    }
    for (var i = 0; i < navigating.length; i++) {
      navigating[i].addEventListener("click", hidemenu, false)
    }
  </script>
</header>
