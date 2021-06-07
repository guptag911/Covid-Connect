<template>
    <div class="box">
        <div class="user-img">
            <figure class="image is-128x128">
                <img class="is-rounded" src="https://img.icons8.com/clouds/2x/user-male.png">
            </figure>
        </div>
        <h3 class="head">Welcome {{myUser.name }}</h3>
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
            <button class="button is-info" style="width: 100%; margin:3px">Edit Profile</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'UserDetailsComponent',
    props: {
        id: String
    },
    data: function () {
        return {
            myUser: {},
            edit: false,
            area: ""
        }
    },
    methods: {
        toggleEdit: function () {
            this.edit = !this.edit;
        },
        save: function () {

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

.head {
    text-align: center;
    font-weight: bolder;
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
