<template>
    <div class="box">
        <div class="user-img">
            <figure class="image is-128x128">
                <img class="is-rounded" src="https://img.icons8.com/clouds/2x/user-male.png">
            </figure>
        </div>
        <h3 class="headWel">Welcome {{myUser.name }}</h3>
        <div style="margin: 5px">
            <div style="text-align: center; margin: 3px">
                <span class="subtitle">Chosen Area: {{myUser.zip}}</span>
                <a v-if="!edit" @click="toggleEdit()"><i class="fas fa-edit"></i></a>
            </div>
            <div v-if="edit" class="edit">
                <input class="input" type="text" v-model="area" placeholder="Enter ZipCode of your area">
                <a @click="save()"><i class="fas fa-check"></i></a>
                <a @click="toggleEdit()"><i class="fas fa-times"></i></a>
            </div>
            <a :href='editProfileUrl'><button class="button is-info" style="width: 100%; margin:3px">View Profile</button></a>
            <button class="button is-danger" style="width: 100%; margin:3px" @click="logout()">Logout!</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { bus, setCookie } from '../main';
export default {
    name: 'UserDetailsComponent',
    props: {
        id: String
    },
    data: function () {
        return {
            myUser: {},
            edit: false,
            area: "",
            editProfileUrl: '/profile?id='
        }
    },
    methods: {
        toggleEdit: function () {
            this.edit = !this.edit;
        },
        save: function () {
            var vm = this;
            var payload = {
                'id': vm.id,
                'fields': {
                    'zip': this.area
                }
            }
            axios.post('/api/v1/update/user', payload).then((resp) => {
                if (resp.data && resp.data.status == 200) {
                    this.toggleEdit();
                    this.myUser.zip = this.area
                    bus.$emit('AREA_CHANGE', this.area);
                }
            })
        },
        profileEdit: function () {
            bus.$emit('PROFILE_EDIT')
        },
        logout: function () {
            setCookie("uid", '', 0);
            bus.$emit('LOGOUT');
        }
    },
    mounted: function () {
        axios.post('/api/v1/user', { 
            id: this.id 
        }).then((resp) => {
            if (resp.data.status === 500) {
                this.myUser = {}
            } else {
                this.myUser = resp.data.data.data;
                this.area = this.myUser.zip;
                this.editProfileUrl +=this.id;
            }
        })
    }
}
</script>

<style scoped>
.box {
    text-align: left;
    margin: 2%;
    width: 100%;
}

.user-img {
    text-align: -webkit-center;
}

.headWel {
    text-align: center;
    font-weight: bolder;
    font-size: 18px;
}

.subtitle {
    text-align: center;
}

i {
    margin: 8px;
}

figure {
    border: 1px solid;
    border-radius: 65px;
}

.edit {
    text-align: center;
    margin: 3px;
    display: flex;
}
</style>
