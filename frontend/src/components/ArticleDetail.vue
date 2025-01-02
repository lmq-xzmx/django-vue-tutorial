<template>
  <div>
    <h2>{{ article.title }}</h2>
    <div v-html="processedBodyHtml"></div>
    <CommentSection :articleId="article.id" />
  </div>
</template>

<script>
import axios from 'axios';
import CommentSection from './CommentSection.vue';

export default {
  name: 'ArticleDetail',
  components: { CommentSection },
  data() {
    return {
      article: {},
      processedBodyHtml: ''
    };
  },
  mounted() {
    const articleId = this.$route.params.id;
    const token = localStorage.getItem('jwt_token'); // 修正此处的键名
    axios.get(`/api/article/${articleId}/`, {
      headers: { Authorization: 'Bearer ' + token }
    })
    .then(response => {
      this.article = response.data;
      this.processedBodyHtml = this.article.body_html.replace(
        /src="\/media/g,
        'src="http://127.0.0.1:8000/media'
      );
    })
    .catch(error => {
      console.error('Error fetching article:', error);
    });
  }
};
</script>
