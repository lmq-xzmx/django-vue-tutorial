<template>
  <div>
    <h2>文章列表</h2>
    <ul>
      <li v-for="article in articles" :key="article.id">
        <router-link :to="{ name: 'ArticlePage', params: { id: article.id } }">
          {{ article.title }}
        </router-link>
        <!-- 添加编辑按钮 -->
        <router-link :to="{ name: 'ArticleEdit', params: { id: article.id } }">
          <button>编辑</button>
        </router-link>
      </li>
    </ul>
    <div>
      <button @click="fetchArticles(previous)" :disabled="!previous">上一页</button>
      <button @click="fetchArticles(next)" :disabled="!next">下一页</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { getCurrentUser } from '../auth';

export default {
  name: 'ArticleList',
  data() {
    return {
      articles: [],
      next: null,
      previous: null
    };
  },
  mounted() {
    this.fetchArticles('http://127.0.0.1:8000/api/article/');
  },
  methods: {
    fetchArticles(url) {
      if (!url) return; // 防止无效的URL请求

      const user = getCurrentUser();
      if (!user || !user.access) {
        console.error('User is not authenticated or access token is missing.');
        this.$router.push({ name: 'Login' }); // 如果未认证，重定向到登录页面
        return;
      }

      const headers = { Authorization: `Bearer ${user.access}` };

      axios.get(url, { headers })
        .then(response => {
          this.articles = response.data.results;
          this.next = response.data.next;
          this.previous = response.data.previous;
        })
        .catch(error => {
          console.error('Error fetching articles:', error);
          if (error.response) {
            if (error.response.status === 401) {
              console.error('Unauthorized access - possibly due to invalid token.');
              this.$router.push({ name: 'Login' }); // 如果未授权，重定向到登录页面
            }
          } else {
            console.error('Network error or server is not reachable.');
          }
        });
    }
  }
};
</script>
