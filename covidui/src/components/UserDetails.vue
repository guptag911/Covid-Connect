<template>
    <div class="box">
        <div class="user-img">
            <figure class="image is-128x128">
                <img class="is-rounded" src="https://img.icons8.com/clouds/2x/user-male.png">
            </figure>
        </div>
        <h3 class="head">Welcome {{myUser.name }}</h3>
        <button class="button is-info" style="width: 100%; margin:1px">Your Posts</button>
        <!-- <hr>
        <p> Name: {{myUser.name}} </p>
        <p> Mobile: {{myUser.number}} </p>
        <p> E-mail: {{myUser.email}} </p>
        <p> ZipCode: {{myUser.zip}} </p>
        <p> Address: {{myUser.address}} </p> -->
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
            myUser: {}
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


figure {
    border: 1px solid;
    border-radius: 65px;
}
</style>
