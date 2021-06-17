<template>
    <div>
        <div class="columns">
            <div class="column users">
                <div class="user"> 
                    <user-details :id='id'></user-details>
                </div>
                <div class="user stats">
                    <covid-stats />
                </div>
            </div>
            <div v-if="!editMode" class="column feedMain">
                <add-post :id="id" :helpTags="helpTags" />
                <feeds-component :helpTags="helpTags" :user="user"/>
            </div>
            <div v-else class="column feedMain">
                <edit-profile />
            </div>
        </div>
    </div>
</template>

<script>
import UserDetailsComponent from '../components/UserDetails.vue'
import CovidStatusVue from './CovidStatus.vue';
import AddPost from './AddPost.vue';
import FeedVue from './Feed.vue';
import axios from 'axios';
import { bus, getCookie } from '../main';
import EditProfileVue from './EditProfile.vue';

export default {
  name: 'Dashboard',
  components: {
      'user-details': UserDetailsComponent,
      'covid-stats': CovidStatusVue,
      'add-post': AddPost,
      'feeds-component': FeedVue,
      'edit-profile': EditProfileVue
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
            user: {},
            editMode: false
      }
  },
  computed: {
      id: function () {
          return getCookie('uid')
      }
  },
  created: function () {
      if (!this.id || this.id == '') {
          window.location = '/';
      }
  },
  mounted: function () { 
      var vm = this;
    axios.get('/api/v1/user/' + this.id).then( (resp)=> {
        if (resp.status == 200) {
            this.user = resp.data.data.data;
        }
    })
    bus.$on('PROFILE_EDIT', function () {
        vm.editMode = true;
    })
    bus.$on('LOGOUT', function () {
        window.location = '/';
    })
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

@media screen and (max-width: 950px) {
    .users {
        max-width: 100%;
    }
    .stats {
        display: none;
    }
    .feedMain {
        margin: 0.5%;
    }

}

.feedMain {
        margin: 1%;
        margin-left: 0px;
        padding-top: 0.5px;
    }
</style>