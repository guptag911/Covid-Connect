import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid: ""
  },
  mutations: {
    setUser: function (id) {
      this.state.uid = id;
    },
    getUser: function () {
      return this.state.uid;
    }
  },
  actions: {
  },
  modules: {
  }
})
