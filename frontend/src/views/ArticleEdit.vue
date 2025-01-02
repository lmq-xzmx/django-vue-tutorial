<template>
    <div>
        <h2>编辑文章</h2>
        <div v-if="article">
            <form @submit.prevent="updateArticle">
                <div>
                    <label for="title">标题:</label>
                    <input type="text" v-model="article.title" id="title" required />
                </div>
                <div>
                    <label for="content">内容:</label>
                    <textarea v-model="article.body" id="content" required></textarea>
                </div>
                <button type="submit">保存</button>
            </form>
        </div>
        <div v-else>
            <p>加载文章中...</p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'ArticleEdit',
        data() {
            return {
                article: null
            };
        },
        mounted() {
            this.fetchArticle();
        },
        methods: {
          fetchArticle() {
            const articleId = this.$route.params.id;
            const token = localStorage.getItem('jwt_token');
            axios.get(`http://127.0.0.1:8000/api/article/${articleId}/`, {
              headers: { Authorization: 'Bearer ' + token }
            })
            .then(response => {
              this.article = response.data;
            })
            .catch(error => {
              console.error('Error fetching article:', error);
            });
          },
          updateArticle() {
            const articleId = this.$route.params.id;
            const token = localStorage.getItem('jwt_token');
            axios.put(`http://127.0.0.1:8000/api/article/${articleId}/`, this.article, {
              headers: { Authorization: 'Bearer ' + token }
            })
            .then(() => {
              alert('文章更新成功！');
              this.$router.push({ name: 'ArticlePage', params: { id: articleId } });
            })
            .catch(error => {
              console.error('Error updating article:', error);
              alert('更新文章时出错，请检查您的权限或联系管理员。');
            });
          }
        }
    };
</script>
