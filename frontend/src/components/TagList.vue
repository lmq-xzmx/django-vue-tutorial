<template>
  <div>
    <h3>标签</h3>
    <ul>
      <li v-for="tag in tags" :key="tag.id">
        {{ tag.text }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TagList',
  data() {
    return {
      tags: []
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/tag/')
      .then(response => {
        this.tags = response.data;
      })
      .catch(error => {
        console.error('Error fetching tags:', error);
      });
  }
};
</script>
