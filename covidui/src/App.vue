<template>
  <div id="app">
    <div v-if="!getStarted" class="start">
      <p class="stitle">Covid Connect</p>
      <p class="ssubtitle">A platform that connects help seekers to the help providers around the globe!</p>
      <button class="button is-link is-large" @click="clicked()">Get Started</button>
    </div>
    <div v-if="getStarted">
      <nav-bar />
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBarVue from './components/NavBar.vue'
import {getCookie } from './main';
export default {
  name: 'App',
  components: {
    'nav-bar': NavBarVue
  },
  data: function () {
    return {
      getStarted: false
    }
  },
  computed: {
      id: function () {
          return getCookie('uid')
      }
  },
  methods: {
    clicked: function () {
      this.getStarted = true;
    }
  },
  mounted: function () {
    if (!this.id  || this.id === '') {
      this.getStarted = false;
    } else {
      this.getStarted = true;
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto&family=Rowdies&display=swap');

#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.stitle {
  font-size: 150px;
  color: white;
  font-family: 'Rowdies', cursive;
}

.ssubtitle {
  font-size: 30px;
  color: white;
  font-family: 'Roboto', sans-serif;
}
.start {
  margin: 2%;
  margin-top: 18%
}


@media screen and (max-width: 950px) {
  .stitle {
    font-size: 80px;
  }
  .ssubtitle {
    font-size: 20px;
  }
}
</style>
