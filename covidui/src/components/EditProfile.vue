<template>
    <div>
        <div class="box">
                <div
                    class="notification"
                    v-if="isError || isSuccess"
                    :class="isError ? 'is-danger' : 'is-success'"
                >
                    <button class="delete" @click="hideNotification()"></button>
                    {{ errorMsg }}
                </div>
                <div class="field">
                    <label class="label">Name</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="text"
                            placeholder="Enter Your Name"
                            v-model="user_data.name"
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-user"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Email</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="email"
                            placeholder="Enter you email address"
                            v-model="user_data.email"
                            disabled
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-envelope"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Mobile Number</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="text"
                            placeholder="Enter Your mobile number"
                            v-model="user_data.number"
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-phone-alt"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label">Address</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="text"
                            placeholder="Enter Your Address"
                            v-model="user_data.address"
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-home"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label">ZipCode</label>
                    <div class="control has-icons-left has-icons-right">
                        <input
                            class="input"
                            type="text"
                            placeholder="Enter Your Area Zip Code"
                            v-model="user_data.zip"
                        />
                        <span class="icon is-small is-left">
                            <i class="fas fa-globe"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <div class="control">
                        <button class="button" style="background: #273d51; color: white" @click="save()" v-on:keyup.enter="save()">
                            Save
                        </button>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "EditProfileComponent",
    computed: {
        'uid': function () {
            return this.$route.query.id || ''
        }
    },
    data: function() {
        return {
            user_data: {},
            isError: false,
            isSuccess: false,
            errorMsg: ""
        }   
    },
    methods: {
        performValidations: function() {
            if (this.user_data.name === "") {
                this.isError = true;
                this.errorMsg = "Please Enter a valid Name";
                return true;
            }
            if (this.user_data.number.length != 10) {
                this.isError = true;
                this.errorMsg = "Mobile Number is invalid!";
                return true;
            }
            if (this.user_data.address.length === 0) {
                this.isError = true;
                this.errorMsg = "Please Enter Address";
                return true;
            }
            if (this.user_data.zip.length !== 6) {
                this.isError = true;
                this.errorMsg = "Zip Code is invalid!";
                return true;
            }
            
            return false;
		},
        save: function () {
            var vm = this;
            if (this.performValidations()) {
                return
            }
            var payload = {
                id: vm.uid,
                fields: {
                    name: this.user_data.name,
                    address: this.user_data.address,
                    zip: this.user_data.zip,
                    number: this.user_data.number
                }
            }
            axios.post('/api/v1/update/user', payload).then((resp) => {
                if (resp.data && resp.data.status == 200) {
                    this.isSuccess = true,
                    this.errorMsg = "Updated Successfully!"
                }
            })
        }
    },
    mounted: function () {
        var vm = this;
        axios.post('/api/v1/user', { 
            id: vm.uid 
        }).then((resp) => {
            if (resp.data.status === 500) {
                this.user_data = {}
            } else {
                this.user_data = resp.data.data.data;
            }
        })
    }
}
</script>

<style scoped>
.box {
    margin: 2%;
    text-align: left;
}

button {
    width: 100%;
}

title {
    padding: 1%;
}
</style>