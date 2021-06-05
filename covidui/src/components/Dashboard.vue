<template>
    <div>
        <nav-bar />
        <div class="columns">
            <div class="column users">
                <div class="user"> 
                    <user-details :id='id'></user-details>
                </div>
                <div class="user">
                    <covid-stats />
                </div>
            </div>
            <div class="column">
                <feeds :id="id" />
            </div>
        </div>
    </div>
</template>

<script>
import NavBarVue from '../components/NavBar.vue';
import UserDetailsComponent from '../components/UserDetails.vue'
import CovidStatusVue from './CovidStatus.vue';
import FeedsVue from './Feeds.vue';

export default {
  name: 'Dashboard',
  components: {
      'nav-bar': NavBarVue,
      'user-details': UserDetailsComponent,
      'covid-stats': CovidStatusVue,
      'feeds': FeedsVue
  },
  props: {
      id: String
  },
  data: function () {
      return {
      }
  },
  computed: {
  
  }
}
</script>

<style scoped>

.user {
    margin: 1%;
}

.users {
    max-width: 30%;
}
</style>