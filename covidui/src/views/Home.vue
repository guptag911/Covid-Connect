<template>
  <div>
    <section class="hero is-small is-info">
      <div class="hero-body">
        <p class="title">Covid Connect</p>
      </div>
    </section>

    <div class="box" v-if="!loginView">
      <div class="notification is-danger" v-if="isError">
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
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input"
            type="password"
            placeholder="Enter you password"
            v-model="user_data.pass"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-key"></i>
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
          <button class="button is-link" @click="signup()">Sign Up</button>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button is-link is-light" @click="toggleLoginView()">
            Already a user! Sign In
          </button>
        </div>
      </div>
    </div>
    <div class="box" v-else>
      <div class="field">
        <label class="label">Email</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input"
            type="email"
            placeholder="Enter you email address"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-envelope"></i>
          </span>
        </div>
      </div>

      <div class="field">
        <label class="label">Password</label>
        <div class="control has-icons-left has-icons-right">
          <input
            class="input"
            type="password"
            placeholder="Enter you password"
          />
          <span class="icon is-small is-left">
            <i class="fas fa-key"></i>
          </span>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button is-link">Sign In</button>
        </div>
      </div>

      <div class="field">
        <div class="control">
          <button class="button is-link is-light" @click="toggleLoginView()">
            New User, Sign Up!
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

export default {
  name: "Home",
  data: function () {
    return {
      user_data: {
        name: "",
        address: "",
        zip: "",
        number: "",
        email: "",
        pass: ""
      },
      loginView: false,
      isError: false,
      errorMsg: "",
    };
  },
  methods: {
    hideNotification: function () {
      this.isError = false;
      this.errorMsg = "";
    },
    toggleLoginView: function () {
      this.loginView = !this.loginView;
    },
    performValidations: function () {
      if (this.user_data.name === "") {
        this.isError = true;
        this.errorMsg = "Please Enter a valid Name";
        return true;
      }
      if ((this.user_data.number).length != 10) {
        this.isError = true;
        this.errorMsg = "Mobile Number is invalid!";
        return true;
      }

      if (this.user_data.zip.length !== 6) {
        this.isError = true;
        this.errorMsg = "Zip Code is invalid!";
        return true
      }
      if (this.user_data.address.length === 0) {
        this.isError = true;
        this.errorMsg = "Please Enter Address";
        return true;
      }
      return false;
    },
    signup: function () {
      if (this.performValidations()) { return }
      axios
        .post('/api/v1/signup', this.user_data).then((resp) => {
          if (resp && resp.data.status === 500) {
            this.isError = true;
            this.errorMsg = resp.data.error;
          } else if (resp && resp.data.status === 200) {
            window['user'] = resp.data.id;
            this.isError = true;
            this.errorMsg = "User Sucessfully Created!"
          }
        })
    }
  },
};
</script>

<style scoped>
.body {
  background: whitesmoke;
}
.box {
  width: 60%;
  margin: auto;
  text-align: left;
  margin-top: 2%;
  margin-bottom: 5%;
}
.button {
  width: 100%;
}
</style>

