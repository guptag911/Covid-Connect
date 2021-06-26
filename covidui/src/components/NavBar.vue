<template>
<nav class="navbar is-dark">
  <div class="navbar-brand">
    <router-link class="navbar-item head"  to="/">
      Covid Connect
    </router-link>
    <a role="button" class="navbar-burger" :class="openMenu ? 'is-active': ''" aria-label="menu" aria-expanded="false" data-target="navbarExampleTransparentExample" @click="menu()">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarExampleTransparentExample" class="navbar-menu" :class="openMenu ? 'is-active': ''">
    <div class="navbar-start" @click="tabChanged()">
      <router-link class="navbar-item" to='/dashboard'>
        Home
      </router-link>
      <router-link class="navbar-item" to="/testimonials">
        Testimonials
      </router-link>
      <router-link class="navbar-item" to="/donate">
        Donate
      </router-link>
    </div>
  </div>
</nav>
</template>

<script>
    export default {
        name: 'NavBar',
        data: function () {
            return {
              currTab: 'home',
              openMenu: false
            }
        },
        computed: {
          tab: function () {
            var currTab = (this.$route.path).replace('/', '');
            return currTab;
          }
        },
        methods: {
          menu: function () {
            this.openMenu = !this.openMenu;
          },
          tabChanged: function () {
            this.openMenu = false;
          }
        }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lobster&family=Open+Sans&display=swap');


.navbar-item {
  font-family: 'Open Sans', sans-serif;
  font-size: 22px;
}

.head {
  font-family: 'Lobster', cursive;
  font-size: 40px;
  color: gold !important;
}
</style>
