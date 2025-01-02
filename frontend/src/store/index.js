import axios from 'axios';

import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    fetchUser({ commit }) {
      // 假设有一个API可以获取当前用户信息
      axios.get('http://127.0.0.1:8000/api/user/')
        .then(response => {
          commit('setUser', response.data);
        })
        .catch(error => {
          console.error('Error fetching user:', error);
        });
    }
  },
  getters: {
    isAuthenticated: state => !!state.user
  }
});
