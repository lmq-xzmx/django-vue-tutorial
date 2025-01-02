<template>
  <div>
    <h3>分类</h3>
    <ul>
      <li v-for="category in categories" :key="category.id">
        {{ category.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CategoryList',
  data() {
    return {
      categories: []
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/category/')
      .then(response => {
        this.categories = response.data;
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  }
};
</script>
