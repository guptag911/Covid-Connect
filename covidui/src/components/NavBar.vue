<template>
<nav class="navbar is-dark">
  <div class="navbar-brand">
    <router-link class="navbar-item head"  to="/">
      Covid Connect
    </router-link>
    <div class="navbar-burger" data-target="navbarExampleTransparentExample">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div class="navbar-start">
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
              currTab: 'home'
            }
        },
        computed: {
          tab: function () {
            var currTab = (this.$route.path).replace('/', '');
            return currTab;
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
