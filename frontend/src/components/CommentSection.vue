<template>
  <div>
    <h3>评论</h3>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        {{ comment.content }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'CommentSection',
  props: ['articleId'],
  data() {
    return {
      comments: []
    };
  },
  mounted() {
    axios.get(`/api/comment/?article=${this.articleId}`)
      .then(response => {
        // 修正：提取 results 中的评论列表
        this.comments = response.data.results;
      })
      .catch(error => {
        console.error('Error fetching comments:', error);
      });
  }
};
</script>
