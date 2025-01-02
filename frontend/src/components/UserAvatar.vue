<template>
  <div>
    <img :src="avatarUrl" alt="User Avatar" v-if="avatarUrl" />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserAvatar',
  data() {
    return {
      avatarUrl: ''
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/avatar/')
      .then(response => {
        // 假设你想显示第一个头像
        if (response.data.results.length > 0) {
          this.avatarUrl = response.data.results[0].content;
        }
      })
      .catch(error => {
        console.error('Error fetching avatar:', error);
      });
  }
};
</script>
