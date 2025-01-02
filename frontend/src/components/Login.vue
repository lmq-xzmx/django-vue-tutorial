<template>
  <div>
    <h2>登录</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">用户名</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">密码</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { login } from '../auth';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    handleLogin() {
      login(this.username, this.password)
        .then(() => {
          this.$router.push({ name: 'Home' });
        })
        .catch(error => {
          this.errorMessage = '登录失败，请检查用户名和密码。';
          console.error(error);
        });
    }
  }
};
</script>


<style scoped>
.error {
  color: red;
}
</style>
