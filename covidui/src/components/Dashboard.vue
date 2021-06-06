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
            <div class="column feedMain">
                <add-post :id="id" :helpTags="helpTags" />
                <feeds-component :helpTags="helpTags" />
            </div>
        </div>
    </div>
</template>

<script>
import NavBarVue from '../components/NavBar.vue';
import UserDetailsComponent from '../components/UserDetails.vue'
import CovidStatusVue from './CovidStatus.vue';
import AddPost from './AddPost.vue';
import FeedVue from './Feed.vue';

export default {
  name: 'Dashboard',
  components: {
      'nav-bar': NavBarVue,
      'user-details': UserDetailsComponent,
      'covid-stats': CovidStatusVue,
      'add-post': AddPost,
      'feeds-component': FeedVue
  },
  props: {
      id: String
  },
  data: function () {
      return {
          helpTags: [
                {
                    id: 0,
                    label: "Need Blood",
                    desc: "This category covers all the blood related requests, like you need blood. Please do spectify the blood group in title."
                },
                {
                    id: 1,
                    label: "Pet Service",
                    desc: "This category covers pet related help, like pet care, pet medical services, etc."
                },
                {
                    id: 2,
                    label: "Food Service",
                    desc: "This category covers food related help needed, like free food at doorstep, etc."

                },
                {
                    id: 3,
                    label: "Medical Help",
                    desc: "This category covers any medical help that you may need, like updating medicine stocks, etc."

                },
                {
                    id: 10,
                    label: "Others",
                    desc: "This category covers all the other kind of help that you want. Please desribe clearly the help you need."
                }
            ],
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

.feedMain {
        margin: 1%;
        margin-left: 0px;
        padding-top: 0.5px;
    }
</style>